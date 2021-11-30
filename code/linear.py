#함수선언
def addData(name):
    katok.append(None)
    klen = len(katok)
    katok[klen-1] = name
def insertData(position,name):
    katok.append(None)
    klen = len(katok)
    for i in range(klen-1,position,-1):
        katok[i] = katok[i-1]
    katok[position] = name
def delData(position):
    klen = len(katok)
    katok[position] = None
    for i in range(position,klen-1):
        katok[i] = katok[i+1]
    del(katok[klen-1])
#전역변수
katok = []
select = -1
#메인
if __name__ == '__main__':
    while select != 4:
        select = int(input('숫자를 입력하세요 : '))
        if select == 1:
            name = input('이름 입력 : ')
            addData(name)
            print(katok)
        elif select == 2:
            position = int(input('자리 입력 : '))
            name = input('이름입력 : ')
            insertData(position,name)
            print(katok)
        elif select == 3:
            position = int(input('자리 입력 : '))
            delData(position)
            print(katok)
        elif select == 4:
            print(katok)
            break
        else:
            print('1~4를 입력하세요')

print(katok)
