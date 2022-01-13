n = int(input("n array : "))
arr = []
div = []
for i in range(n) :
    arr.insert(i,int(input()))
print(arr)
a = int(input("Enter a number : "))
j = 0
for i in range(n):
    if arr[i]%a==0 :
        div.insert(j,arr[i])
        j=j+1
print("Divisible number of",a,"is",div)
