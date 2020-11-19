
# 1~100 summation

i = 0
result = 0

while i <= 100:

    if i == 50:
        i += 1
        continue
    if i % 2 == 0:
        result += i

    i += 1

# observe the value of i when cycle shut down
print("i=%d"%i)
print(end="result = %d"%result)  # 可以这样表示不换行
print("fdsaf")

print("result = %d"%result , end="")  # 也可以这样表示不换行
print("fdsaf")
