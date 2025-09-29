def greet(name):
    """
    Greets a person with the given name.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}!"

print(greet.__doc__)




def calculate_area(length, width):
    """
    Calculates the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return length * width
print(calculate_area.__doc__)



def multi_line(line):
    """
    This function demonstrates a multi-line docstring.
    
    It can span multiple lines and provide detailed information
    about the function's purpose, parameters, and return values.
    
    Parameters:
    line (str): A line of text.

    Returns:
    str: The same line of text.
    """
    return line
print(multi_line.__doc__)