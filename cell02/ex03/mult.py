#!/usr/bin/env python3
def main():
    print("Enter the first number : ")
    n1 = int(input())
    print("Enter the second number : ")
    n2 = int(input())

    result = n1 * n2
    print(f"{n1} x {n2} = {result}")
    if result > 0:
        print("The result is positive.")
    elif result < 0:
        print("The result is negative.")
    else:
        print("The result is positive and negative.")

main()