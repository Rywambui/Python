def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    
    print ("Number of Upper case characters : ", d["UPPER_CASE"])
    print ("Number of Lower case Characters : ", d["LOWER_CASE"])

string_test('My Name Is Irene Wambui')
string_test('I am excited about learning python')
string_test('I am a Student of 30 Days')

