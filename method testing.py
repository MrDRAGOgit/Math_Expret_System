import math
import time
import tracemalloc
import math as mt


def funct(A, x):
    return A[0]*mt.exp(-A[3]*mt.pow(x-A[2], 2)+A[1])


def integration():
    filepath = "intergration_input.csv"
    N = 20
    A = []
    x = []
    h = []
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        for text in input_file:
            text = text[:-2]
            A.append(text.split(";"))
    for line in A:
        for i in range(len(line)):
            line[i] = float(line[i].replace(",", "."))
        x.append(line[4])
        h.append((line[5]-line[4])/N)
    for i in range(len(A)):
        A[i] = A[i][:-2]
    for i in range(len(A)):
        tracemalloc.start()
        start = time.time()
        ans = 0
        xi = float(x[i])
        hi = h[i]
        for j in range(N):
            ans += (hi/6) * (funct(A[i], xi) + 4*funct(A[i], xi + (hi/2)) + funct(A[i], xi+hi))
            # ans += hi * funct(A[i], xi)
        print(ans)
        end = time.time()
        print((end - start) * 10 ** 3, "ms, ", tracemalloc.get_traced_memory(), "bits")
        tracemalloc.stop()


start = time.time()

integration()

end = time.time()
print((end-start) * 10**3, "ms")
