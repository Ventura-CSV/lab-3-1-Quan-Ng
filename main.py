def main():
    ##################################################
    # Comlete your code here
    ##################################################
    number = int(input('Enter your input: '))

    """
    Make your code here
    """
    if (number < 50):
        range = 1
    
    elif (50<= number <100):
        range = 2
    
    elif (number >= 100):
        range = 3

    print(f'Range: {range}')
    ########################################
    # Do not delete the return statement
    ########################################
    return range


if __name__ == '__main__':
    main()
