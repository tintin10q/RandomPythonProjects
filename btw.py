#
#
# done = False
#
# while done is not True:
#     number_input = input("Give a price:")
#     try:
#         number_input = int(number_input)
#         if number_input <= 0:
#             print('Number needs to be more then 0')
#         else:
#             print("Price with btw is:", number_input * 1.21)
#             done = True
#     except ValueError:
#         print("Please enter a number!")


def add_up(x, y):
    return x + y


print(add_up(10))
