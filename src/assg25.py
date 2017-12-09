string=input("enter a string")
l=len(string)
res_string=""
for i in range(0,l,+1):
    if(i%2==0):
        res_string=res_string+string[i]
print("res_string=",res_string)
p=len(res_string)
rev=res_string[::-1]
print("expectedoutput=",rev)