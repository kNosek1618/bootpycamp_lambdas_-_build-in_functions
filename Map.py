
# main function of map !

# map(function, iterable)

#####################################################

# THE SAME RESULT WITH USING 'MAP' and 'DEF' function

nums = (2,4,6,8,10)

doubles = map(lambda x: x*2, nums)
print(list(doubles))

##################################

def check(*args):
    score = []
    for a in args:
        a *= 2
        score.append(a)
    return score

print(check(*nums))

###################################

# def cube(*args):
#     score = 0
#     for arg in args:
#         score += arg
#     return score
#
# nums = (2,4,6,8,10)
# print(cube(*nums))


# doubles = map(lambda x: x*2 ,nums)
