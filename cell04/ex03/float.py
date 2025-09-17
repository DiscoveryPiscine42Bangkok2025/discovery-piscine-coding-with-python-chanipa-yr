num = input("Give me a number:")
try:
    val = float(num)
    if val.is_integer():
        print("This number is an integer")
    else:
        print("This number is a decimal.")
except ValueError:
    print("This is not avalid number.")