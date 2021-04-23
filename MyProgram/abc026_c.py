N = int(input())
B = [int(input()) for _ in range(N-1)]

figure = [[] for _ in range(N)]

for i in range(N-1):
    figure[B[i]-1].append(i+1)

salary = [0]*N

for i in range(N-1, -1, -1):
    if len(figure[i]) == 0:
        salary[i] = 1
    elif len(figure[i]) == 1:
        n = figure[i][0]
        salary[i] = salary[n]*2 + 1
    else:
        minSalary = float('INF')
        maxSalary = -float('INF')
        for j in figure[i]:
            if minSalary > salary[j]:
                minSalary = salary[j]
            if maxSalary < salary[j]:
                maxSalary = salary[j]
        salary[i] = maxSalary + minSalary + 1

print(salary[0])