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

#만들어둔 노드를 처음부터 끝까지 출력하는 함수
current = node1
print(current.data,end=" ")
while current.link != None:
    current = current.link
    print(current.data,end=" ")

