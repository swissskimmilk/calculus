from math import *
    
def newtonsmethod():
    
    # Change-able variables
    max_iterations = 20
    epsilon = 10**(-6)
    
    # Input
    f = input("Function: ")
    df = input("Derivative of function: ")
    x0 = int(input("Initial x-value: "))
    
    # Initial values
    n = 1
    xn = x0
    fx = eval(f, None, {'x':xn})
    dfx = eval(df, None, {'x':xn})

    # Output lists
    n_list = ["n"]
    xn_list = ["xn"]
    fx_list = ["fx"]
    dfx_list = ["dfx"]
    
    while n <= max_iterations and abs(fx) > epsilon and dfx != 0:
        
        xn_list.append(xn)
        xn = xn - (fx / dfx)

        n_list.append(n)
        fx_list.append(fx)
        dfx_list.append(dfx)
        
        n += 1
        fx = eval(f, None, {'x':xn})
        dfx = eval(df, None, {'x':xn})
        
        print(n, xn, fx, dfx, "\n")
        
    # Format output
    def list_length(lst):
        length = 0
        for i in range(1, len(lst)):
            lst[i] = round(lst[i], 5)
            if len(str(lst[i])) > length:
                length = len(str(lst[i]))
        return length
    
    n_length = list_length(n_list)
    xn_length = list_length(xn_list)
    fx_length = list_length(fx_list)
    dfx_length = list_length(dfx_list)
            
    for i in range(len(n_list)):
        print("{:<{}}{:<{}}{:<{}}{:<{}}".format(n_list[i], n_length + 1, 
                                                xn_list[i], xn_length + 1,
                                                fx_list[i], fx_length + 1,
                                                dfx_list[i], dfx_length + 1))
        
    if  abs(fx_list[-1]) <= epsilon:
        print("Found solution.")
    elif dfx == 0:
        print("Derivative is 0. No solution found.")
    elif n == max_iterations:
        print("Exceeded maximum iterations. No solution found.")
 
newtonsmethod()