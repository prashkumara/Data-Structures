number=20
str=''
if number <0:
    print("ffffff")
while number>0:
    if number == 10:
        str = str + "a"
        print(str)
        break
    if number == 11:
        str = str + "b"
        print(str)
        break
    if number == 12:
        str = str + "c"
        print(str)
        break
    if number == 13:
        str = str + "d"
        print(str)
        break
    if number == 14:
        str = str + "e"
        print(str)
        break
    if number == 15:
        str = str + "f"
        print(str)
        break

    remainder = number%16
    quot = number//16
    str=str+str()
