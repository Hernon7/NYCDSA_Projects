import pandas as pd
import pymysql
# time
import time

# os 
import os
os.environ["JAVA_HOME"] = "C:\Program Files\Java\jdk1.8.0_221"
os.environ["SPARK_HOME"] = "C:\spark\spark-2.3.3-bin-hadoop2.7"

# data science imports
import math
import numpy as np
import pandas as pd


#from scipy.sparse import csr_matrix
#from urllib.request import urlopen

# utils import
#!pip install fuzzywuzzy
#from fuzzywuzzy import fuzz

# visualization imports
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import findspark
findspark.init('C:\spark\spark-2.3.3-bin-hadoop2.7')

from pyspark import SparkContext

# import pyspark.sql related packages
from pyspark.sql import SparkSession, SQLContext, Row
from pyspark.sql.functions import UserDefinedFunction, explode, desc, col, lower, lit
from pyspark.sql.types import StringType, ArrayType

# import pyspark.ml related packages
from pyspark.ml.recommendation import ALS
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
from pyspark.ml.tuning import TrainValidationSplit, ParamGridBuilder
from pyspark.ml.evaluation import RegressionEvaluator

# spark = SparkSession.builder.master("local[*]").getOrCreate()
# spark = SparkSession.builder.master("local").appName("test").getOrCreate()
# spark = SparkSession \
#     .builder \
#     .appName("movie recommendation") \
#     .getOrCreate()
# get spark context
# sc = spark.sparkContext(conf=conf)
# sqlContext = SQLContext(sc)



class connector:
    '''This class will contain everything related to the Database,
    Connect, Insert, Display data from the database
    '''

    def __init__(self):
        # Connect the database once the class created
        #####################################
        ###### Change Before run ############
        host = "database-1.cbfgky4ljfg6.us-east-2.rds.amazonaws.com"
        port = 3306
        dbname = "movie"
        user = "admin"
        password = "12345678"
        self.connection = pymysql.connect(
            host, user=user, passwd=password, db=dbname)

    def test(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT VERSION()')
        self.connection.commit()

    def get_dataframe(self, tablename):
        cursor = self.connection.cursor()
        sql = "SELECT * FROM %s" % (tablename)
        cursor.execute(sql)
        table_rows = cursor.fetchall()
        if tablename == 'movie_df':
            moviedf = pd.DataFrame(table_rows)
            # movieRDD = sqlContext.createDataFrame(moviedf)
            # movieRDD = movieRDD.selectExpr("MovieId as item","Movie_title as title")
            return moviedf
        elif tablename == 'rating_df':
            ratingdf = pd.DataFrame(table_rows)
            # ratingRDD = sqlContext.createDataFrame(ratingdf)
            # ratingRDD = ratingRDD.selectExpr("UserId as user","MovieId as item","Rating as rating")
            return ratingdf