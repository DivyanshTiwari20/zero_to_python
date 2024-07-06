'''
There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.
Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.


Example 1:
Input: n = 4, time = 5
Output: 2
Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
After five seconds, the 2nd person is holding the pillow.
'''
def passThePillow(n,time):
    completed=time//(n-1)
    remaining=time%(n-1)

    ans=0
    # if num of rounds are odd pillow will move right to left and then minus remaining part, minus bcoz we are in right side or at last digit of list eg: 1,2,3. lst digit=3 , (n-remaining) means it will move like 3 then 2 then 1
    if completed%2!=0:
        ans=n-remaining
    else:
        # if num of rounds are odd pillow will move left to right and then add remaining part, add bcoz we are on left side or at first digit of list eg:1,2,3. first digit=1 , (remaining +1) means it will start from first person then move to remaining 
        ans=remaining+1

    return ans

print(passThePillow(6,11))
