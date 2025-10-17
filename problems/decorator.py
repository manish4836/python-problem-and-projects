# 1. Outer Function: decorator_function
def log_start_end(func):
    
    # 2. Inner Wrapper Function: *args aur **kwargs se yeh har tarah ke arguments le sakta hai
    def wrapper(*args, **kwargs):
        print(f"--- Function {func.__name__} is starting ---")
        
        # Original function ko call karo
        result = func(*args, **kwargs)
        
        print(f"--- Function {func.__name__} has finished ---")
        return result
    
    # 3. Wrapper function ko return karo
    return wrapper

# Decorator ko use karne ka tareeka: '@' syntax
@log_start_end
def calculate_sum(a, b):
    # Yeh hamara original function hai jise hum change nahi kar rahe
    return a + b

# Function ko call karo
sum_result = calculate_sum(10, 5)
print(f"Result: {sum_result}")


@log_start_end
def multiplication(a, b):
    return a * b

product_mult = multiplication(5,5)
print(f"product: {product_mult}")