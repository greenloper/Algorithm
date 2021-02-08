s=input()
list=[0]*2

if s[0]=="0":
    list[0]+=1
else: list[1]+=1

for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        if s[i+1]=="1":
            list[0]+=1
        else:
            list[1]+=1

print(min(list))