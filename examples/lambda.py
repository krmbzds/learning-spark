square = lambda x: x**2
square(5)

add = lambda x,y: x+y
add(3, 5)

integers = list(range(1, 11))

list(map(square, integers))

list(map(lambda x: x**3, integers))

def my_map(func, lis):
    results = []
    for element in lis:
        results.append(func(element))
    return results

filter(lambda x: x%2==0, integers)

def my_filter(func, lis):
    # TODO: write filter

def my_reduce(func, lis):
    result = lis[:]
    for index in range(len(lis)-1):
        result[index+1] = func(result[index], result[index+1])
    return lis[-1]

my_reduce(lambda x,y: x+y, integers)
