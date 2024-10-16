def input_number(str):
    flag = False
    while not flag:
        try:
            number = int(input(f"Enter {str} :"))
            if number > 0:
                flag = True
            else:
                print("You need enter the positive number")
        except ValueError:
            print("Invalid value !!!")
    return number


x = input_number("x")
y = input_number("y")


def isPerpectNumber(n):
    gcd_list = [1]
    for i in range(2, n):
        if n % i == 0:
            gcd_list.append(i)
    s = 0
    for j in range(len(gcd_list)):
        s += gcd_list[j]
    if s == n:
        return True
    else:
        return False


result = 0
for i in range(x, y + 1):
    if isPerpectNumber(i):
        result += i
print("Sum of perpect in range [x,y]: ", result)
