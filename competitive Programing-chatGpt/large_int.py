'''
Question: Write a function that takes two integers and returns the larger of the two.
'''
#Using bulit in fuction
def largeint(a,b):
    return max(a,b)

print(largeint(6,8))

#logic behind using the bulit in function

def largeint(a,b):
    if a>b:
        return a
    else :
        return b
print(largeint(6,8))