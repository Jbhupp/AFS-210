def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum
    print(odd_sum)

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum
    print(even_sum)

def loop1Rec(num = 0,odd_sum = 0):
    # Duplicate the loop1 function using recursion
    print(num)
    if num < 20:
        # then check if its odd,
        if num % 2 == 0: 
            return(loop1Rec(num+1, odd_sum + num))
        else:
            return(loop1Rec(num+1, odd_sum))
    else: 
        return odd_sum
    print( odd_sum)
print(loop1Rec(0))
    

def loop2Rec(num = 0,even_sum = 0):
    # Duplicate the loop2 function using recursion
    if num < 20: 
        # then check if its even,
        if num % 2 == 0: 
            return(loop1Rec(num+1, even_sum + num))
        else:
            return(loop1Rec(num+1, even_sum))
    else: 
        return even_sum
        print(even_sum)
print(loop2Rec(0))