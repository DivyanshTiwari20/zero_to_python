'''
function to find first occurrence of a target element in a 
sorted list using binary search. 
'''


'''
Eg: 
 
let list =[3,4,5,6,7,8] # list should be shorted

first define lower and upper values

here:
lower=0 and upper = 8 

then:
find the mid term (lower+upper//2) #use // to get int only

then check:
if target==mid :
    stop
else:
    check target < mid or target>mid
        if target<mid:
            upper== mid

        esle:
            target>mid:
                lower==mid
'''

def binary_search(lst,target):
    lower,upper=0,len(lst)-1
    while lower<=upper:
        mid=(lower+upper)//2

        if lst[mid] == target:
            return mid
        elif(lst[mid]<target):
            lower=mid+1

        else:
            upper=mid-1
            
    return -1
print(binary_search([1,2,3,4,5],5))

        