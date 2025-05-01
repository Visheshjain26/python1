def convert_temp():
    fahrenheit = [32, 68, 100, 212, 50]
    print("Fahrenheit temperatures:", fahrenheit)
    celsius = [round((i - 32) * 5 / 9, 2) for i in fahrenheit]
    print("Celsius temperatures:", celsius)