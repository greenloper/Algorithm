s=list(map(int, input()))
result=s[0]

for i in range(0, len(s)-1):
    if s[i]<=1 or result<=1:
        result+=s[i+1]
    else:
        result*=s[i+1]

print(result)
