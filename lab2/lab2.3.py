N = int(input("N > 2 \nN = "))
A = float(input("A < B \nA = "))
B = float(input("B = "))

R = (B - A) / (N - 1)
print("R = " + str(R))

for i in range(N):
    print(str(A), end="; ")
    A += R