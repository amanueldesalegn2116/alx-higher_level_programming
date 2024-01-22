#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print X Elememts Of A List.
    Args:
        my_list (list): The List To Print Elements From.
        x (int): The Number Of Elements Of my_list To Print.
    Returns:
        The Number Of Elements Printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
