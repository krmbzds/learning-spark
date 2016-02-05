nums = sc.parallelize([1, 2, 3, 4])
squared = nums.map(lambda x: x * x).collect()
