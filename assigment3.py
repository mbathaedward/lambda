def math_operations(num1,num2):

    """
    This funtion takes two numbers(num1,num2):
    calculates sum of the two numbers using lambda funtion
    calculates their product using lambda funtion 
    Returns sum and product as tuple

    """
    sum_lambda = lambda a ,b: a + b
    product_lambda = lambda a,b: a * b

    return sum_lambda(num1,num2),product_lambda(num1,num1)

def main():
    """
    main function to interat with the user :
    prompts the user for two numbers.
    calls the 'math_operations' function with input numbers.
    prints the sum and the product  of the numbers.
    """
    try:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        #call the math_operations function
        sum_result,product_result = math_operations(num1, num2)

        #prints the result 
        print(f"sum is {sum_result}")
        print(f"product is {product_result}")
    except ValueError:
        print("invalid input.please enter a valid numbers.")
    
    #execution of the main function

if __name__ == "__main__":
    main()







