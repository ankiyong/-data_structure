class Node():
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = "기용"

node2 = Node()
node2.data = "수지"
node1.link = node2

node3 = Node()
node3.data = "지수"
node2.link = node3

print(node1.link.data)

newNode = Node()
newNode.data = '제니'
newNode.link = node2
node1.link = newNode
print(node1.link.data)




