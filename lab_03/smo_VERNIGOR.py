import math
#2 варіант
n = 3

#коефіцієнти передачі, доля потоку вимог, що надходить до СМОі
e = [0.35, 1, 0.6]

#матриця ймовірностей
p = [[0, 0.35, 0],
     [1, 0.4, 1],
     [0,  0.6, 0]]

#інтенсивність обслуговування вимог кожним каналом СМОі
mu = [0.2, 0.2, 0.4]

#кількість вимог в мережі СМО
N = 7

#кількість каналів обслуговування в кожній СМОі
r = [3, 1, 1]

#нормуючий множник
cN = 0.0050794523540588525

#допоміжні функції для обчислення ймовірності стану системи та нормуючого множника
def p(i, k):
    tmp = (e[i]/mu[i])**k
    if (k < r[i]):
            return tmp/math.factorial(k)
    else:
            return tmp/(math.factorial(r[i])*((r[i])**(k-r[i])))

#обчислення нормуючого множника
def c(N):
    result = 0
    for i in range(N + 1):
        tmp = 0
        for j in range(N + 1 - i):
            tmp = tmp + p(1, j)*p(2, N - j - i)
        result = result + p(0, i)*tmp
    return 1/result
print("c(N) = ", c(N))
print("")

#обчислення ймовірності того, що в СМОі j вимог
def pSMO(i, j):
    cN = c(N)
    result = 0
    if i == 0:
        for a in range(N + 1 - j):
            result = result + p(0, j)*p(1, a)*p(2, N - j - a)
    if i == 1:
        for a in range(N + 1 - j):
            result = result + p(0, a)*p(1, j)*p(2, N - j - a)
    if i == 2:
        for a in range(N + 1 - j):
            result = result + p(0, a)*p(1, N - j - a)*p(2, j)
    return result*cN

#перевірка правильності обчислення нормуючого множника, сума усіх ймовірностей СМОі = 1
def cNtest():
    for j in range(n):
        sum = 0
        for i in range (N+1):
            sum = sum + pSMO(j, i)
        print("Сума PСМО", j + 1, " = ", sum)
cNtest()
print("")

#1)середня кількість вимог у черзі СМОі
def L(i):
    result = 0
    for j in range(r[i] + 1, N + 1):
        result = result + (j - r[i])*pSMO(i, j)
    return (result)
L = [L(0), L(1), L(2)]
print("Середня кількість вимог у черзі:")
print(L)
print("")

#2)середня кількість зайнятих пристроїв СМОі
def R(i):
    result = 0
    for j in range(r[i]):
        result = result + (r[i] - j) * pSMO(i, j)
    return r[i] - result
R = [R(0), R(1), R(2)]
print("Середня кількість зайнятих пристроїв:")
print(R)
print("")


#3)середня кількість вимог СМОі
def M(i):
    return L[i] + R[i]
M = [M(0), M(1), M(2)]
print("Середня кількість вимог:")
print(M)
print("")

#4)інтенсивність вихідного потоку вимог у СМОі
def Lam(i):
    return R[i]*(1/mu[i])
Lam = [Lam(0), Lam(1), Lam(2)]
print("Інтенсивність вихідного потоку вимог:")
print(Lam)
print("")

#5)середній час перебування вимоги у СМОі
def T(i):
    return M[i]/Lam[i]
T = [T(0), T(1), T(2)]
print("Середній час перебування вимоги:")
print(T)
print("")

#6)середній час очікування в черзі СМОі
def Q(i):
    return L[i]/Lam[i]
Q = [Q(0), Q(1), Q(2)]
print("Середній час очікування в черзі:")
print(Q)
print("")

