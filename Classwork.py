def main():
    # problem1()
    # problem2()
    # problem3()
    problem4()


def problem1():
    mode = input("Inside or Outside mode!:\n")
    n = int(input("Enter a number:\n"))
    while mode.lower() == "outside":
        if n <= 1 & n >= 10:
            print("True")
            break
        else:
            print("False")
            break

    while mode.lower() == "inside":
        if n >= 1 & n <= 10:
            print("True")
            break
        else:
            print("False")
            break

def problem2():
    words = []
    while 1 == 1:
        user = input("Enter a word:\n")
        if user == "=":
            print(*words, sep=", ")
            break
        else:
            words.append(user)

def problem3():
    x = 0
    while x >= 0:
        y = x * 10
        x += 1
        if mun1 != mun1:
            while x >= 0:
                mun1 = int(input("Enter a number:\n"))
                if mun1 <= y + 2 & mun1 >= y - 2:
                    print("True")
                    break

                else:
                    print("False")
                    break
        else:
            break


def problem4():
    number1 = [34, 4, 32, 7]
    number2 = [4, 44, 23, 17]
    number3 = [90, 78, 52, 9]
    sub = number1(1) - number1(2)
    print(sub)


if __name__ == '__main__':
    main()