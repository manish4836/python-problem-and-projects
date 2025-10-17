import random
def read_and_optimization():
    try:
        with open("data.txt", "r") as file:
            all_lines = file.readlines()   
            clean_lines = [line.strip() for line in all_lines]
            random_lines = random.sample(clean_lines, 3)
        return tuple(random_lines)
    except FileNotFoundError:
        return ("Error: 'data.txt' file not found. Please create the file with content.")

result = read_and_optimization()
print(result)