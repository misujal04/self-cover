queue=[]
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue : ",queue)

frontelement=queue[0]
print("Peek",frontelement)

print("{PoP",queue.pop(0))

print("After the poping element",queue)

isEmpty=not bool(queue)

print("Queue is Empty",isEmpty)
