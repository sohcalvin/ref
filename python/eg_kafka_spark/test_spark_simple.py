from pyspark import SparkContext
from pyspark.rdd import RDD



logFile = "./spark_test_data.txt"  # Should be some file on your system
sc = SparkContext("local", "Simple App")


def simpleExample():
    logData = sc.textFile(logFile).cache()
    numAs = logData.filter(lambda s: 'a' in s).count()
    numBs = logData.filter(lambda s: 'b' in s).count()



    # logData.saveAsTextFile("g.rdd")
    print("Lines with a: %i, lines with b: %i" % (numAs, numBs))


# def matrixExample() :





sc.stop()

