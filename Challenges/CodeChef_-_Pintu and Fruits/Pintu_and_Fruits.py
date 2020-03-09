testCasesCount = int(input())
while testCasesCount>0:
    temp = input()
    templst = temp.split(" ")
    basketsCount = int(templst[0])
    fruitsTypeCount = int(templst[1])
    temp1 = input()
    temp2 = input()
    fruitsType = temp1.split(" ")
    fruitsCost = temp2.split(" ")
    fruitsType = [int(i) for i in fruitsType]
    fruitsCost = [int(i) for i in fruitsCost]

    arr = [0 for i in range(fruitsTypeCount)]
    for i in range(len(fruitsType)):
        arr[fruitsType[i]-1]=arr[fruitsType[i]-1]+fruitsCost[i]
    m = min(i for i in arr if i > 0)
    print(m)
    testCasesCount = testCasesCount-1
