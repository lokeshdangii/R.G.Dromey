# s = 2+4+6 +.....

n = int(input("enter the no. of terms to be sum up : "))
series = []
ele = 2
for i in range(0,n):
    series.append(ele)
    ele = ele+2
print("series of numbers : ",series)
sum = sum(series)
print("the sum of the numbers is : ", sum)