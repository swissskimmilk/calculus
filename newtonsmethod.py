from math import *

def get_real_root(rt_term, x):
    root = eval(rt_term, None, {'x':x})
        
    if type(root) == complex:
        
        if "/" in rt_term:
            
            start = rt_term.find("**(") + 3
            end = len(rt_term)-1
            
            base = rt_term[:start-3]
            fraction = rt_term[start:end]
            numerator = fraction[:fraction.find("/")]
            denominator = fraction[fraction.find("/")+1:]
    
            temp_root = eval("{}**{}".format(base, numerator), None, {"x":x})
            
            if int(denominator) % 2 == 1 and temp_root < 0:
                root = eval("{}**(1/{})".format(-temp_root, denominator), None, {"x":x}) * -1
                return root
            elif int(denominator) % 2 == 0 and temp_root < 0:
                return None
            else:
                root = eval("{}**(1/{})".format(temp_root, denominator), None, {"x":x})
                return root
    else:
        return root

def solve_eq(eq, x):
    eq = eq.replace(" ", "")
    
    index = 0
    rt_indices = []

    while index < len(eq):
        index = eq.find('**(', index)
        if index == -1:
            break
        rt_indices.append(index)
        index += 3 # +3 because len('**(') == 3

    rt_terms = {} # dict of first_index:term
    rt_ranges = [] # list of first_index:last_index for each term

    for rt_index in rt_indices:
        rt_term = ""
        
        char_before = 0
        # check for characters before **(
        for i in range(rt_index-1, -1, -1):
            if eq[i] in ["+", "-", "*", "/"]:
                break 
            else:
                rt_term = eq[i] + rt_term
                char_before += 1
            
        rt_term = rt_term + "**("
            
        char_after = 0
        # check for characters after **(
        for i in range(rt_index+3, len(eq)):
            if eq[i] == ")":
                rt_term = rt_term + eq[i]
                char_after += 1
                break
            else:
                rt_term = rt_term + eq[i]
                char_after += 1
        
        rt_ranges.append([rt_index - char_before, rt_index + 3 + char_after])
        rt_terms[rt_index - char_before] = rt_term
        
    for term in rt_terms:
        rt_terms[term] = get_real_root(rt_terms[term], x)    

    # Create equation_index 
    # Indices represent individual char or rt_term
    equation_index = list(range(len(eq)))
    for rt_range in rt_ranges:
        count = rt_range[0] # need placeholder index to represent rt equation
        equation_index.append(count)
        while count < rt_range[1]:
            equation_index.remove(count)
            count += 1
    equation_index.sort()

    # Create equation string for eval
    equation = ""
    for index in equation_index:
        if index in rt_terms:
            equation += str(rt_terms[index])
        else:
            equation += str(eq[index])
    
    output = eval(equation, None, {"x":x})
    return output

def newtonsmethod(f, df, x0):
    # Change-able variables
    max_iterations = 20
    epsilon = 10**(-6)
    
    # Initial values
    n = 1
    xn = x0
    fx = solve_eq(f, xn)
    dfx = solve_eq(df, xn)

    # Output lists
    n_list, xn_list, fx_list, dfx_list = ["n"], ["xn"], ["fx"], ["dfx"]
    
    while n <= max_iterations and abs(fx) > epsilon and dfx != 0:
        xn_list.append(xn)
        xn = xn - (fx / dfx)

        n_list.append(n)
        fx_list.append(fx)
        dfx_list.append(dfx)
        
        n += 1
        fx = solve_eq(f, xn)
        dfx = solve_eq(df, xn)
        
    # Format output
    def list_length(lst):
        length = len(lst[0])
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
    if  abs(fx) <= epsilon:
        print("Found solution.")
    elif dfx == 0:
        print("Derivative is 0. No solution found.")
    elif n > max_iterations:
        print("Exceeded maximum iterations. No solution found.")
        
f = input("Function: ")
df = input("Derivative: ")
x0 = float(input("Initial x-value: "))
newtonsmethod(f, df, x0)