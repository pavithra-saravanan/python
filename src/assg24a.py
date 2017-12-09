string1=input("please enter a string")
s=len(string1)
count=0
for i in range (0,s,+1):
    if(string1[i]>='A') and (string1[i]<='Z'):
        count=count+1
        print(string1[i])
print(count)