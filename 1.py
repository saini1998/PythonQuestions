# 1. Find the counts of elements of an unsorted integer array which are equal to the average of all elements of that array.

a = [1,1,1]
avg = 0
count = 0
N = 3
sum = 0 
for i in range(N):
    sum = (sum + a[i]) 
   
avg = sum / N
for i in range(N):
    if avg == a[i]:
        count = count + 1

print(count)




