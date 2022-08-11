class MyCircularQueue:
    def __init__(self, size: int):
        # Write code here

     def enqueue(self, value: int) -> bool:
        if(isfull)
         return 
    else
    rare = (rare + 1)%n
    size = size + 1
    return x

    def dequeue(self) -> bool:
       if (is empty)
          return 
    else
    x = Q[front]
    front = (front+1)%n
    size = size - 1
    return x

    def get_front(self) -> int:
        # Write code here

    def get_rear(self):
        # Write code here

    def is_empty(self):
        return x
    else
    x = Q[front]
    front = (front+1)%n
    size = size - 1
    return x

    def is_full(self):
        return x
    else
    rare = (rare + 1)%n
    size = size + 1
    return x


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
data = []
for item in input().split(','):
    item = item.strip()
    if item == '-':
        data.append([])
    else:
        data.append([int(item)])
obj = MyCircularQueue(data[0][0])
result = []
for i in range(len(operations)):
    if i == 0:
        result.append(None)
    elif operations[i] == "enqueue":
        result.append(obj.enqueue(data[i][0]))
    elif operations[i] == "get_rear":
        result.append(obj.get_rear())
    elif operations[i] == "get_front":
        result.append(obj.get_front())
    elif operations[i] == "dequeue":
        result.append(obj.dequeue())
    elif operations[i] == "is_full":
        result.append(obj.is_full())
    elif operations[i] == "is_empty":
        result.append(obj.is_empty())

print(result)
