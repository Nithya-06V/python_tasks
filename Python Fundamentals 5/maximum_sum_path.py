
matrix=[[1,3,1],[1,5,1],[4,2,1]]
m=len(matrix)
n=len(matrix[0])
dp=[[0]*n for _ in range(m)]
dp[0][0]=matrix[0][0]
for i in range(1,m):
    dp[i][0]=dp[i-1][0]+matrix[i][0]
for j in range(1,n):
    dp[0][j]=dp[0][j-1]+matrix[0][j]
for i in range(1,m):
    for j in range(1,n):
        dp[i][j]=matrix[i][j]+max(dp[i-1][j],dp[i][j-1])
path=[]
i=m-1
j=n-1
while i>0 or j>0:
    path.append(matrix[i][j])
    if i==0:
        j-=1
    elif j==0:
        i-=1
    elif dp[i-1][j]>=dp[i][j-1]:
        i-=1
    else:
        j-=1
path.append(matrix[0][0])
path.reverse()
print("Maximum path sum:",dp[m-1][n-1])
print("Path:",path)
