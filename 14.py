import math
print("welcome to my calculator")
a=int(input("please enter a number: "))
op=input("please enter operation: ")
if op=="sqrt":
    result=math.sqrt(a)
if op=="sin":  
    result=math.sin(a)
if op=="cos":   
    result=math.cos(a)
if op=="tan":   
    result=math.tan(a)
if op=="cot":  
    result=math.cot(a)
if op=="factorial":  
    result=math.factorial(a)
if op=="+":
    b=int(input("please enter another number: ")) 
    result=a+b
if op=="-":
    b=int(input("please enter another number: ")) 
    result=a-b
if op=="*":
    b=int(input("please enter another number: ")) 
    result=a*b
if op=="/":
    b=int(input("please enter another number: ")) 
    resulte=a/b
print(result)
