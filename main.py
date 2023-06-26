def main():
  
    # Comlete your code here
    celsius_temp = float( input("Temperature value in degree Celsius: " ))  
    fehrenhiet_temp = celsius_temp * 1.8 + 32
    print("The Fahrenheit equivalent of x = ", fehrenhiet_temp)
    return celsius_temp, fehrenhiet_temp


if __name__ == '__main__':
    main()
