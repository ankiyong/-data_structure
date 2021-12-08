#전역변수
memory = []
pre,current,head = None,None,None
dataArray = ['지수','제니','로제','윈터','카리나']
#함수선언
class Node():
    def __init__(self):
        self.data = None
        self.link = None
def printNodes(start):
    current = start
    print(current.data,end=" ")
    while current.link != None:
        current = current.link
        print(current.data,end=" ")
    print()

def insertNodes(find,insert):
    global pre,current,head

    if find == head.data:
        node = Node()
        node.data = insert
        pre = current
        pre.link = node
        return
    current = head
    while current.link != None:
        current = current.link
        pre = current
        if current.data == find:
            node = Node()
            node.data = insert
            pre = current
            pre.link = node
            return
    #마지막 노드에 삽입
    node = Node()
    node.data = insert
    current.link = node


#메인실행
if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)
    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

printNodes(head)


