def main():
    n1 = int(input("Give me the first number : "))
    n2 = int(input("Give me the second number : "))
    u = int(n1 / n2)

    print("Thank you!")

    print(f"{n1} + {n2} = {n1 + n2}")
    print(f"{n1} - {n2} = {n1 - n2}")
    print(f"{n1} / {n2} = {u}")
    print(f"{n1} * {n2} = {n1 * n2}")

main()