# Angelo Smith
# 11/16/22
# Question 2 1-10 are true while everything else is false.

def check_number(Choose):
    if Choose > 10:
        return False
    elif Choose < 1:
        return False
    else:
        return True


Chk_nbr = int(input("Input a number"))
answer = check_number(Chk_nbr)
print(answer)

