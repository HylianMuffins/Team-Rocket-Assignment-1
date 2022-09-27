# this is code for control flow 
# this was charu's code 


if operator_one == '+' or "-" and operator_two == "*" or "/": 

    if operator_two == "*":
        stored_val = myNum(num1,num3)
    else: 
        stored_val = myDiv(num2,num3)
    
    if operator_one == "+":
        final_val = myAdd(num1,stored_val)
    else:
        final_val = mySub(num1,stored_val)
    
else: 
    if operator_one == "+":
        stored_val = myAdd(num1,num2)     
    elif operator_one == "-":
        stored_val = mySub(num1,num2)
    elif operator_two == "*":
        stored_val = myMul(num1,num2)
    else:
        stored_val= myDiv(num1,num2)
    
    if operator_two == "+":
        final_val = myAdd(stored_val,num3)
    elif operator_two == "-":
        final_val = mySub(stored_val,num3)
    elif operator_two == "*":
        final_val=myMul(stored_val,num3)
    else:
        final_val = myDiv(stored_val,num3)

        
return final_val
