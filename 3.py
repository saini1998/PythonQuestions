
# 3. Find the average of largest and smallest numbers in an unsorted integer array?
# Eg. [1, 4, 3, 2] => average = (1+4)/2 = 2.5
# [1, 4, 3, 4] => average = (1+4+4)/3 = 3

a = [1,4,3,4]
N = 4
maxA = max(a)
minA = min(a)
countMax = 0
countMin = 0
for i in range(N):
    if maxA == a[i]:
        countMax = countMax + 1
    if minA == a[i]:
        countMin = countMin + 1
den = countMax + countMin
avg = ((maxA * countMax) + (minA * countMin)) / den
print(avg) 