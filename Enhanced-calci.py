def log_operations(func):

    def wrapper(*args,**kwargs):
        print(f'\n[LOG] executing {func.__name__} with arguments {args}')
        result=func(*args,**kwargs)
        print(f'[LOG] Result: {result}\n')
        return result
    
    return wrapper

# calculator function code

def calculator_memory():
    last_result=None

    def get_last():
        return last_result
    
    def clear_last():
        nonlocal last_result
        last_result=None
    
    def set_last(value):
        nonlocal last_result
        last_result=value
    
    return get_last,clear_last,set_last

get_last,clear_last,set_last=calculator_memory()

# Operations

@log_operations
def add(a,b):
    result=a+b
    set_last(result)
    return result

@log_operations
def subtract(a,b):
    result=a-b
    set_last(result)
    return result

@log_operations
def product(a,b):
    result=a*b
    set_last(result)
    return result

@log_operations
def divide(a,b):
    if b==0:
        raise ValueError("cannot divide with zero")
    result=a/b
    set_last(result)
    return result

@log_operations
def power(a,b):
    if b < 0:
        raise ValueError("Exponent must be non-negative")
    result=a**b
    set_last(result)
    return result

def main():
    operations={
        1:add,
        2:subtract,
        3:product,
        4:divide,
        5:power
    }

    while True :

        print("================== ENHANCED CALCULATOR ==================\n")
        print("1. Add")
        print("2. Subtract")
        print("3. Product")
        print("4. Division")
        print("5. Power")
        print("6. Show last result")
        print("7. clear last result")
        print("8.Exit")

        try :
            choice=int(input("Enter your choice: "))

            if choice==8:
                print("Thanks for using our calculator")
                break
            
            if choice==7:
                clear_last()
                print("\nLast result cleared\n")
            if choice==6:
                print(f"\nLast result: {get_last()}\n")
                continue

            if choice not in operations :
                print("Invalid choice! please try again ...")
                continue

            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))

            operations[choice](a,b)

        except ValueError as e :
            print("Error: ",e,"\n")
                 

#calling main function
if __name__=='__main__':
    main()