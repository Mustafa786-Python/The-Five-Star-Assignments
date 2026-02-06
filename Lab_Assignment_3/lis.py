def even_generator(limit):
    list1 = []
    for i in range(1, limit + 1, 2):
        list1.append(i)
        yield list1

for num in even_generator(10):
    print(num)
