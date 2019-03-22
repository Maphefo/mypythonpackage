def sum_array(array):

    '''Return sum of all items in array'''
    return array.sum()

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n <=1:
        return n
    else:
        return n+(n-1)

def factorial(n):

    '''Return n!'''
    result = 1
    count = 2

    while count <= n:
        result = result * count
        count = count + 1
    return result

def reverse(word):

    '''Return word in reverse'''
    return word[::-1]
