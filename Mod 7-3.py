# Angelo Smith
# 11/16/22
# Question 3 this will multiply the number list within the random numbers I put within the parenthesis.

def multiplication(numb_list):
    equal = 2
    for z in numb_list:
        equal *= z
    return equal


print(multiplication((8, 2, 3, 90, 9)))