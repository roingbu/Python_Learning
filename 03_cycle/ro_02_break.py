# print "hello python" 5 times
# 1~100 summation

i = 0
result = 0

while i <= 100:
    
    if i % 2 == 0:
        result += i
    i += 1
    if i==99:
        break  # stop the current cycle!

# observe the value of i when cycle shut down
print("i=%d"%i)
print("result = %d"%result)
