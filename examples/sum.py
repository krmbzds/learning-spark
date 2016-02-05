numbers = sc.parallelize(range(1, 101))
sum = numbers.reduce(lambda x, y: x + y)
