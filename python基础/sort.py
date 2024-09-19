import random

a = []
for i in range(0, 10):
    a.append(random.randint(1, 100))
    # a.append(int(input("Please input a number: ")))

print("Numbers are:")
print(a)

for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print("Sorted numbers are:")
print(a)
