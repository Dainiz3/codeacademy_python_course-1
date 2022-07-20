# def say_hello(name):
#     return f"Hello {name}"

# def say_hello2(name):
#     return f"Howdy {name}"

# def greet_bob(greeter_func):
#     return greeter_func("Bob")


# print(greet_bob(say_hello))
# print(greet_bob(say_hello2))


# def parent():
#     print("Printing from the parent() function")

#     def first_child():
#         print("Printing from the first_child() function")

#     def second_child():
#         print("Printing from the second_child() function")

#     second_child()
#     first_child()

# parent()

# def first_child():
#     return f"Hi, I am Emma"

# first_child()

# def parent(num):
#     def first_child():
#         return f"Hi, I am Emma"

#     def second_child():
#         return "Call me Liam"

#     if num == 1:
#         return first_child
#     else:
#         return second_child



# my_function = parent(1)
# print(my_function())

# import time

# def timer(func):
#     def wrapper():
#         time_start = time.time()
#         func()
#         time.sleep(5)
#         time_end = time.time()
#         print(f" program took {time_end - time_start} seconds")
        
#     return wrapper

# @timer
# def say_whee():

#     print("Whee!")


# # say_whee = my_decorator(say_whee)

# say_whee()


def decor1(func):
        def wrap():
               print("************")
               func()
               print("************")
        return wrap
def decor2(func):
        def wrap():
               print("@@@@@@@@@@@@")
               func()
               print("@@@@@@@@@@@@")
        return wrap
     
# @decor1
# @decor2
def sayhellogfg():
         print("Hello")

sayhellogfg = decor2(sayhellogfg)
sayhellogfg = decor1(sayhellogfg)

# def saygfg():
#          print("GeekforGeeks")
         
sayhellogfg()
# saygfg()