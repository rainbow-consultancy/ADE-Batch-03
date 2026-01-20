# functions | methods

# def my_function():
#     print("Hello World")

# my_function()

# def my_function():
#     return "Hello World"

# print(my_function())


def add(a, b):
    return a+b if (a+b) % 2 == 0 else None

# print(add(10, 30))
# print(add(100, 330))
# print(add(10000, 3031))

# def sub(a, b):
#     return a - b

# print(sub(40, 10))

# list comprehension

even = []
for i in range(1, 11):
    if i%2 == 0:
        even.append(i)
# print(even)


new_even = [i for i in range(1, 11) if i%2 == 0]
# print(new_even)

def add(a: int, b: int) -> None:
    return a+b if (a+b) % 2 == 0 else None


# write a function in python where it will take a string as argument
# and then gives the count of it

def get_length(name: str) -> str:
    return f"{name} - {len(name)}"

# print(get_length("Sandeep"))
# print(get_length("Anil"))


# anonymous functions or lambda functions

def is_even(num: int) -> bool:
    return num % 2 == 0

# print(is_even(100)) # --> True
# print(is_even(91)) # --> False

is_even = lambda num: num%2 == 0
# print(is_even(100)) # --> True
# print(is_even(91)) # --> False

# map
def get_square(n):
    return n**2

nums = [2, 3, 4, 5]
result = list(map(lambda n: n**2, nums))
# print(result)


# filter
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = tuple(filter(lambda n: n%2 == 0, nums))
# print(result)


# Nested Functions

# def outer():
#     def inner():
#         print("This is an inner function")
#     inner() # calling inner function
#     print("This is an outer function")
    
# outer()

def outer():
    def inner():
        print("This is an inner function")
    inner() # calling inner function
    print("This is an outer function")

# outer()

def calculate_salary(gross_salary: int, tax_rate: float) -> int:
    def apply_tax(salary: int):
        return gross_salary * tax_rate
    tax_amount = apply_tax(gross_salary)
    net_amount = gross_salary - tax_amount
    return f"Net Salary - {int(net_amount)}, Tax deducted by Govt - {int(tax_amount)}"

# print(calculate_salary(2_00_000, 0.34))
# print(calculate_salary(3_00_000, 0.34))
