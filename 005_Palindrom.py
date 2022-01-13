def palindrom(num) :
    if len(num)<2 :
        pal=1
        print("A single digit number? Yikes!")
    elif len(num)>=2 :
        if len(num)%2==0:
            for i in range(int(len(num)/2)):
                if num[i]==num[len(num)-(i+1)]:
                    pal=1
                else:
                    pal=0
        elif len(num)%2==1:
            for i in range(int((len(num)-1)/2)):
                if num[i]==num[len(num)-(i+1)]:
                    pal=1
                else:
                    pal=0
                    
    if pal==1 :
        print("Given number is a palindrom")
    else :
        print("Given number is not a palindrom")

print("Insert number to check it's a palindrom number or not!")
a = input()
palindrom(a)
