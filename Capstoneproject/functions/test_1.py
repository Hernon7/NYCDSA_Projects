import db_connector
import pandas as pd
import engine
from pyspark.sql import SparkSession, SQLContext, Row
from py4j.java_gateway import JavaGateway, GatewayParameters
gateway = JavaGateway(gateway_parameters=GatewayParameters(port=25335))
gateway=JavaGateway()

# from pyspark.ml.evaluation import RegressionEvaluator
# from pyspark.ml.tuning import TrainValidationSplit, ParamGridBuilder
# from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
# from pyspark.ml.recommendation import ALS
# from pyspark.sql.types import StringType, ArrayType
# from pyspark.sql.functions import UserDefinedFunction, explode, desc, col, lower, lit
# from pyspark.sql import SparkSession, SQLContext, Row
# from pyspark import SparkContext
# import findspark
# import matplotlib.pyplot as plt
# import seaborn as sns
import numpy as np
# import math
# import pandas as pd
# import pymysql
# # time
# import time

# # os
# import os
# os.environ["JAVA_HOME"] = "C:\Program Files\Java\jdk1.8.0_221"
# os.environ["SPARK_HOME"] = "C:\spark\spark-2.3.3-bin-hadoop2.7"

# # data science imports


# #from scipy.sparse import csr_matrix
# #from urllib.request import urlopen

# # utils import
# #!pip install fuzzywuzzy
# #from fuzzywuzzy import fuzz

# # visualization imports
# plt.style.use('ggplot')

# findspark.init('C:\spark\spark-2.3.3-bin-hadoop2.7')


# # import pyspark.sql related packages

# # import pyspark.ml related packages


spark = (SparkSession.builder
         .master("local[*]")
         .appName("movie recommendation")
        #  .config("spark.driver.memory","8g")
        #  .config("spark.executor.memory","8g")
         .getOrCreate())
# get spark context
spark.conf.set("spark.sql.execution.arrow.enabled", "true")
sc = spark.sparkContext
sqlContext = SQLContext(sc)


db = db_connector.connector()
ratingdf = db.get_dataframe('rating_df')
ratingdf = ratingdf.to_json(orient='columns') #json
ratingRDD = spark.read.json(ratingdf).rdd

moviedf = db.get_dataframe('movie_df')
moviedf = moviedf.to_json(orient='columns') #json
movieRDD = spark.read.json(moviedf).rdd

eng = engine.sparkconverter()

# moviedfL = eng.sparkrating(moviedf).limit(10)
# ratingdfL = eng.sparkrating(ratingdf).limit(10)
# ratingRDD = eng.sparkrating(ratingdf) #
#  returns ratingRDD
# movieRDD = eng.sparkmovie(moviedf) # returns movieRDD

sets = eng.split_sets(ratingRDD, [0.60, 0.20, 0.20])

eng.hotmodel(sc, sets, movieRDD)

# spark.stop()