lines = sc.parallelize(['Hello world', 'Hi'])
words = lines.flatMap(lambda line: line.split(' ')).collect()
