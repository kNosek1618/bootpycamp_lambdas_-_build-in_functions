
def square(num): return num * num

square2 = lambda num: num * num

add = lambda a,b: a + b

##################################

print(square(9)) # 81

print(square2(8)) # 64

print(add(2,3)) # 5

#################################

print(square.__name__)  # square
print(square2.__name__) # <lambda>
print(add.__name__)     # <lambda>

#################################

