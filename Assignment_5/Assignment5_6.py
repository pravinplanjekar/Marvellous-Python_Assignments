"""
Celsius to Fahrenheit Converter
Accept temperature in Celsius and convert it to Fahrenheit using the formula:
F = (C × 9/5) + 32
Expected Input:
Enter temperature in Celsius: 25
Expected Output:
Temperature in Fahrenheit: 77.0°F
"""

def Celciustofahrenheit(fNo):
    F = (fNo * 9/5) + 32

    return F

def main():
    print("Enter temperature in Celsius:")
    Value = float(input())

    fRet = Celciustofahrenheit(Value)
    print(f"Temperature in fahrenheit is  : {fRet}")


if __name__ == "__main__":
    main()

