
m = int(input("Enter M: "))
q = int(input("Enter Q: "))
n = int(input("Enter bits: "))

a = 0
q1 = 0
mod = 2 ** n

for i in range(n):

    q0 = q % 2

    if q0 == 0 and q1 == 1:
        a = a + m
    elif q0 == 1 and q1 == 0:
        a = a - m

    a = a % mod

    if a >= mod // 2:
        a = a - mod

    t = a % 2

    q = (q // 2) + (t * (mod // 2))

    a = a // 2
    q1 = q0

print("Product =", a * mod + q)
