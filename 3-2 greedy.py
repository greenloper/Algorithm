n, m, k= map(int, input().split())
input=list(map(int, input().split()))

input=sorted(input, reverse=True)
first=input[0]
second=input[1]

cnt=0
cnt=int(m/(k+1))*k
cnt+=m%(k+1)

sum=0
sum=cnt*first
sum+=(m-cnt)*second

print(sum)