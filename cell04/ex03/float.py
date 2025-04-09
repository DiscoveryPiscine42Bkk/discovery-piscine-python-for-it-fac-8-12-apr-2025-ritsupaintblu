def main():
    n = input("Give me a number : ")
    p = n.find(".")
    if p > -1:
        if int(n[p+1:]) > 0:
            print("This number is a decimal.")
        else:
            print("This number is an integer.")
    else:
        print("This number is an integer.")

main()