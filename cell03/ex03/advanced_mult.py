import sys
def main():
    if len(sys.argv) > 1:
        print("none")
    else:
        i = 0
        while i <= 10:
            j = 0
            p = ""
            while j <= 10:
                result = i * j
                p += f"{result} "
                j +=1
            print(f'Table de {i}: {p}')
            i += 1

main()