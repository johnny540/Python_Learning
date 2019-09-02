"""SimpleApp.py"""
from pyspark.sql import SparkSession

logFile = "D:\EDUCATION\Tutorial\Python\pyPrac\input.txt"  # Should be some file on your system
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print(type(logData))
logData.count()	

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()