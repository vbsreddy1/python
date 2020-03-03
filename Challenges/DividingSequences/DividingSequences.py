n = int(input("Enter the size of the array:"))
arr=[]
for i in range(n):
    temp = int(input())
    arr.append(temp)

lsa = []
temparr = []
print(arr)
for i in range(n):
    temparr.append(arr[i])
    for j in range(i+1, n):
        #for k in range(len(temparr)):
            if arr[j]%temparr[k] == 0:
                temparr.append(arr[j])
                #print(temparr)
    if len(lsa) < len(temparr):
        lsa=temparr[:]
    temparr.clear()

print(lsa)
