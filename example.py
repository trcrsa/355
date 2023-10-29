def main():
    a = int(input("Enter number: "))
    b = int(input("Enter second number: "))

    sum = sumOf(a,b)

    print(f"The sum of {a} and {b} is: {sum}")

def sumOf(a,b):
    return a + b

if __name__ == "__main__":
    main()