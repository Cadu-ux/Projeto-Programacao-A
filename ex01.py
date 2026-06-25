n = int(input())

print(f"Digite os {n} elementos do primeiro array:")
array1 = [int(input()) for _ in range(n)]

print(f"Digite os {n} elementos do segundo array:")
array2 = [int(input()) for _ in range(n)]

print("\nArrays intercalados:")
for i in range(n):
    print(array1[i])
    print(array2[i])