def dectooct(num):
    temp= num
    i = 1
    sum = 0
    while temp!=0:
        rem = int(temp%8)
        sum = sum +i*rem
        i= i*10
        temp= temp/8
    print("Octal Number =", sum)
    return sum


num = int(input("Enter any Number "))
dectooct(num)