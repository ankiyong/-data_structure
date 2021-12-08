class Node():
    def __init__(self):
        self.data = None
        self.link = None


node1 = Node()
node1.data = '기용'

node2 = Node()
node2.data = "수지"
node1.link = node2

node3 = Node()
node3.data = '지은'
node2.link = node3


#노드 삽입

newNode = Node()
newNode.data = '지수'
newNode.link = node2
node1.link = newNode

#노드 삭제
node1.link = node2
del newNode

current = node1
print(current.data,end=" ")
while current.link != None:
    current = current.link
    print(current.data,end=" ")
