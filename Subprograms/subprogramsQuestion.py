#Question 1
# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Alice"))
# print(greet("Bob"))

def repeat_message(message, times):
    for i in range(times):
        print(message)

time = int(input("How many times?: "))
message = input("What is your message?: ")

repeat_message(message, time)
