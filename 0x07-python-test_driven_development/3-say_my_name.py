#!/usr/bin/python3
'''Contains a say_my_name function
'''


def say_my_name(first_name, last_name=""):
    '''Prints a given first and last name

    Args:
        first_name (str): The first name
        last_name (str): The last name

    Raises:
        TypeError: first_name and last_name are not strings.
    '''
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print('My name is {} {}'.format(first_name, last_name))
