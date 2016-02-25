# Transformations are lazy
rdd = sc.textFile("README.md")
rdd.first() #=> '#\xa0Learning Spark'
rdd.count() #=> 3

# Transformation versus Action
# Actions produce results
# .first() .count() <-- actions
# Saving is also an action

rdd1 = sc.parallelize([1,2,3,4,5,6,7,8,9,10])
evens = rdd1.filter(lambda x: x%2==0)
odds  = rdd1.filter(lambda x: x%2!=0)

evens.collect() #=> [2, 4, 6, 8, 10]
odds.collect() #=> [1, 3, 5, 7, 9]

# Union Operation
odds.union(evens).collect() #=> [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

inputRDD = sc.textFile("examples/lambda.py")
lambdas = inputRDD.filter(lambda x: "lambda" in x)
functions = inputRDD.filter(lambda x: "def" in x)
comments = inputRDD.filter(lambda x: "#" in x)
