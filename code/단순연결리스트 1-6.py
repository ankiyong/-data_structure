#전역변수
memory = []
current,pre,head = None,None,None
dataArray = ['지수','제니','로제','윈터','카리나']
select = -1
#함수선언
class Node():
    def __init__(self):
        self.data =None
        self.link = None

def printNodes(start):
    current = start
    print(current.data,end=" ")
    while current.link != None:
        current = current.link
        print(current.data,end=' ')
    print()
def insertData(find,insert):
    global pre,current,head
    if head.data == find:
        node = Node()
        node.data = insert
        node.link = head
        head = node
        return
    current = head
    while current.link != None:
        current = current.link
        pre =  current
        if current.data == find:
            node = Node()
            node.data = insert
            node.link = pre.link
            pre.link = node
            return
    node = Node()
    node.data = insert
    current.link = node

def delData(deldata):
    global pre,current,head
    if head.data == deldata:
        current = head
        head = current.link
        del(current)
        return
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deldata:
            pre.link = current.link
            del(current)
            return


#메인함수

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

# insertData('로제','기용')
# printNodes(head)

while select != 3:
    select = int(input('숫자 입력 : '))
    if select == 1:
        find = input('찾는 이름 : ')
        name = input('넣을 이름 : ')
        insertData(find,name)
    elif select == 2:
        deldata = input('삭제할 이름 : ')
        delData(deldata)
    elif select == 3:
        pass
    else:
        print('1~3 입력해주세요')
    printNodes(head)

