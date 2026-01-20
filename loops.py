# loops

# print(10)
# print(10)
# print(10)
# print(10)
# print(10)


# 2. loop definitions

# 1. for loop
# 2. while loop


# range(start : stop : step)

# for i in range(0, 10, 1):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)

# for i in range(10):
#     print(i)


# print odd numbers from 11 to 51 (include)

# for i in range(11, 52):
#     if i%2 != 0:  # odd
#         print(i)
        

# 2. while loop

# print 1-10 numbers on to the output screen

start = 1
end = 10

# while start <= end:
#     print(start)
#     start = start + 1


# name = input("Enter the name: ")

# logic to count no.of vowels in that name
    
# "python"  --> a, e, i, o, u  --> 1
# "Lion" --> 2    

# vowels = ('a', 'e', 'i', 'o', 'u')

# cnt = 0
# for i in name.lower():
#     if i in vowels:
#         cnt = cnt + 1

# print(cnt)

# sandeep - 3

# 2 * 1 = 2
# 2 * 2 = 4
# .
# .
# 2 * 10 = 20

# 3 * 1 = 3
# 3 * 2 = 6


# for i in range(1, 11):
#     print(f"2 * {i} = {2*i}")

# for i in range(2, 6):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i*j}")
#     print("------------------------------")
    

# for i in range(5): # (0, 1, 2, 3, 4)
#     for j in range(3): # (0, 1, 2)
#         print(f"{i}-{j}")

# for i in range(1, 10):
#     print("*" * i)


# --> print only even tables like 2, 4, 6, 8

for i in range(2, 9):
    if i % 2 == 0:
        for j in range(1, 11):
            print(f"{i} * {j} = {i*j}")
        print("-------------------------")