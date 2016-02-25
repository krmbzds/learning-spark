numbers = sc.parallelize([0,1,1,1,0,1,0,1,0,0])

def return_zero(x):
    return x == 0

def return_one(x):
    return x == 1

numbers.filter(return_zero).collect()
numbers.filter(return_one).collect()
