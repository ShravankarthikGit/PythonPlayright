#concatenation  +

# 1 when we use + between 2 numeric values , it will perform addition
print(10+10)   # 20 valid
print(10.5+12.0)  # 22.5  valid
print(10+10.5)   #20.5 valid


#2  when we use + between strings, it will perform concatenation

print("welcome" + " python")   #welcome python


#3  when we use +  between one boolean and numeric then also perform addition operation
print(True+5)   #6    True=1  False=0
print(False+5)  #5
print(True+True)  #2


#4 we cannot concatenate 2 different types

print(10+"welcome")    # not valid bcoz 2 values are different type  TypeError:
print(10.5+'welcome')  # not valid bcoz 2 values are different type  TypeError:
print(True+"welcome")  # not valid bcoz 2 values are different type  TypeError:







