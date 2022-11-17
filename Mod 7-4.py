# Angelo Smith
# 11/16/22
# Question 4 this will append the number to appear in a unique way.

def unique_list(num_list):
    my_list = []
    for z in num_list:
        if z not in my_list:
            my_list.append(z)
    return my_list


print(unique_list([1, 3, 3, 3, 6, 2, 3, 5]))
