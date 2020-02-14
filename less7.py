#LOOPS
#conditional statements(>, <, >=, <=, !=, ==)
print(5>6)
print(5<6<4)
print(4!=3)
print('abc'=='cda')
#logical operators(not, and , or) in operator presidence
#Python's boolean constants are capitalized: True and False
a = True
b = False
print (not a) # a= true so not a=false
print(a and b) #both have to be true/false so false
print(not b)
print(a or b)

#IF statement
code_greeting= 'hello'
if code_greeting =='hello' or code_greeting =='hi':
    print("hi, you good?")
#if else
#indetation is very important , collon before statement
if 5<6:
    if 5>7:
            print('5<6')
    else:
            print("not true!")
#el if .. used for conditions that didn't pass and you want to include another condition
age = 20
if (age > 1 and age < 19):
    print(age)
elif (age > 5 and age < 10):
    print(age+1)
else:
    print(age-1)
    #example 2
var = 100
if var == 200:
   print ("1 - Got a true expression value")
   print (var)
elif var == 150:
   print ("2 - Got a true expression value")
   print (var)
elif var == 100:
   print ("3 - Got a true expression value")
   print (var)
else:
   print ("4 - Got a false expression value")
   print (var)

print ("Good bye!")

# TERNARY-Operator...used when there is a decision to be made when assigning a value to a valuable
#uses if and else in line
code_greetings = "Hello"
me = "hi" if code_greetings == "Hello" or code_greetings =="Hi" else "Hey"
print (me)





        
  





