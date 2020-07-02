def Queue() :

    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.append(5)
    print(queue)

    while queue:
        print("Get Value : ", queue.pop(0))

Queue()