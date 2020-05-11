# import packages
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.tuning import TrainValidationSplit, ParamGridBuilder
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
from pyspark.ml.recommendation import ALS
from pyspark.sql.types import StringType, ArrayType
from pyspark.sql.functions import UserDefinedFunction, explode, desc, col, lower, lit
from pyspark.sql import SparkSession, SQLContext, Row
from pyspark import SparkContext
import findspark
# import matplotlib.pyplot as plt
# import seaborn as sns
import numpy as np
import math
import pandas as pd
import pymysql
# time
import time

# os
import os
os.environ["JAVA_HOME"] = "C:\Program Files\Java\jdk1.8.0_221"
os.environ["SPARK_HOME"] = "C:\spark\spark-2.3.3-bin-hadoop2.7"

# data science imports


#from scipy.sparse import csr_matrix
#from urllib.request import urlopen

# utils import
#!pip install fuzzywuzzy
#from fuzzywuzzy import fuzz

# visualization imports
# plt.style.use('ggplot')

findspark.init('C:\spark\spark-2.3.3-bin-hadoop2.7')


# import pyspark.sql related packages

# import pyspark.ml related packages


spark = (SparkSession.builder
         .master("local[*]")
         .appName("movie recommendation")
         .config("spark.driver.memory","8g")
         .config("spark.executor.memory","8g")
         .getOrCreate())
# get spark context
sc = spark.sparkContext
sqlContext = SQLContext(sc)


class sparkconverter:
    def __init__(self):
        # self.tablename = tablename
        pass

    def sparkmovie(self, df):
        movieRDD = sqlContext.createDataFrame(df)
        # movieRDD = sc.broadcast(moviedf)
        movieRDD = movieRDD\
            .withColumnRenamed("0", 'item')\
            .withColumnRenamed("1", 'title')
        # movieRDD = movieRDD.selectExpr("MovieId as item", "Movie_title as title")
        return movieRDD


    def sparkrating(self, df):
        ratingRDD = sqlContext.createDataFrame(df)
        # ratingRDD = sc.broadcast(ratingdf)
        ratingRDD = ratingRDD\
        .withColumnRenamed("0", "user")\
        .withColumnRenamed("1", "item")\
        .withColumnRenamed("2", "rating")
        # ratingRDD = ratingRDD.selectExpr(
        #     "UserId as 0", "MovieId as 1", "Rating as 2")
        ratingRDD.show()
        return ratingRDD
    
        ### user defined functions
    def split_sets(self, ratings, proportions):
        '''
        input: the dataset and the proportion list
        output: the split datasets
        '''
        split = ratings.randomSplit(proportions, seed=42)
        return {'training': split[0], 'validation': split[1], 'test': split[2]}
    
    def calc_se(self, rating, user_factor, item_factor):
        '''
        Squared Error (SE) for a single rating and prediction
        '''
        prediction = user_factor.T.dot(item_factor)
        return (rating - prediction) ** 2
    
    def hotmodel(self, sc, sets, movieRDD):
        '''
        training a super hot model
        '''
        als = ALS(coldStartStrategy="drop")
        param_grid = ParamGridBuilder() \
        .addGrid(als.rank, [6, 8]) \
        .addGrid(als.maxIter,[8, 10, 12]) \
        .build()

        evaluator = RegressionEvaluator(
            metricName="mse",
            labelCol="rating",
            predictionCol="prediction")

        tvs = TrainValidationSplit(
            estimator=als,
            estimatorParamMaps=param_grid,
            evaluator=evaluator,
        )

        model = tvs.fit(sets['training']) ## should we save the model?
        best_rank = model.bestModel.rank
        best_iterations = model.bestModel._java_obj.parent().getMaxIter()
        print('hotmodel part 1')

        prediction = model.transform(sets['test'])
        prediction.alias('p')\
            .join(movieRDD.alias('m'), col('p.item') == col('m.item'))\
                .select([col('p.user'), col('m.title'), col('p.prediction'), col('p.rating')])

        mse = evaluator.evaluate(prediction)
        print("MSE = {}".format(mse))

        '''
        hot model's tinder date
        '''
        rating59169 = [
                (118661, 9), # Avengers
                (371746, 9),  # Iron Man 2008
                (94625, 9),  # Akira
                (1563738, 2), # One day 2011
                (800369, 8),  # Thor
                (1981115, 9), # Thor: The Dark World
                (3501632, 9), # Thor: Ragnarok
                (120338, 3), # Titanic
                (98635, 2), # When Harry Met Sally
                (125439, 3), # Notting Hill
                (332280, 1) # The Notebook
            ]
        
        user59169 = ratingRDD.groupBy().max('user').first()['max(user)'] + 1
        user59169DF = spark.createDataFrame\
        ([Row(user=user59169, item=r[0], rating=r[1]) for r in rating59169])
        user59169DF = user59169DF.select('user','item','rating')
        # user59169DF = sc.parallelize(user59169DF)
        new_model = ALS(rank=best_rank, maxIter=best_iterations, coldStartStrategy="drop")\
            .fit(ratingRDD2)

        unseen_movies = movieRDD.alias('m')\
            .join(user59169DF.alias('r'), col('m.item') == col('r.item'), how='left_anti')\
                .select('item')
        unseen_movies_user = unseen_movies.withColumn("user", lit(user59169))

        print('hot model part 2')

        spark.conf.set("spark.sql.crossJoin.enabled", "true")
        unseen_ratings = new_model.transform(unseen_movies_user)

        unseen_ratings_titles = unseen_ratings.alias('r')\
                        .join(movieRDD.alias('m'), col('r.item') == col('m.item'))\
                        .select(['user', 'title', 'prediction'])

        ratings_per_movie = ratingRDD.groupBy('item').count()
        enough_ratings = ratings_per_movie.filter(col('count') < 500)
        enough_ratings.show()

        
        training_10 = unseen_ratings.alias('r')\
            .join(enough_ratings.alias('e'), col('r.item') == col('e.item'), how='left_anti')\
            .select(['item', 'user', 'prediction']).orderBy(col('prediction').desc())

        training_100.alias('t').join(movieRDD.alias('m'), col('t.item') == col('m.item'))\
            .select(['user', 'title', 'prediction'])\
                .orderBy(col('prediction').desc()).show(10, truncate=False)
    
    # spark.stop()