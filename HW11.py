"""Задание 1"""
september = {'Варламов В.А.', 'Иванов И.Н.', 'Викторов А.В.', 'Петров И.Н.'}
october = {'Ляшко А.В.', 'Викторов А.В.', 'Сидоров В.Н.', 'Варламов В.А.'}

print(set.union(september, october))


"""Задание 1.2"""
september = {'Варламов В.А.', 'Иванов И.Н.', 'Викторов А.В.', 'Петров И.Н.'}
october = {'Ляшко А.В.', 'Викторов А.В.', 'Сидоров В.Н.', 'Варламов В.А.'}
C = october - set.intersection(september, october)
print(C)


"""Задание 2"""
A = {}
B = {'W': 'write', 'R': 'read', 'X': 'execute'}
for i in range(int(input())):
    x = input().split()
    A[x[0]] = [B[i] for i in x[1:]]
for i in range(int(input())):
    a, n = input().split()
    print('OK' if a in A[n] else 'Access denied')
