<<<<<<< HEAD:competitive Programing-chatGpt/recurision/tower_of_hanoi.py
<<<<<<< HEAD
=======
>>>>>>> b1e894c8f4f88706e4e6472a63308c77b347ce99:Competitive_programing/recurision/tower_of_hanoi.py
"""
    Solves the Tower of Hanoi problem recursively.
    
    Args:
        n (int): The number of disks.
        source (str): The name of the source peg.
        auxiliary (str): The name of the auxiliary peg.
        destination (str): The name of the destination peg.
"""

def towe_of_hanoi(n,source,auxiliary,destination):
    if n==1:
        print( f"Move disk 1 from {source} to {destination}")
        return 
    
    towe_of_hanoi(n-1,source,auxiliary,destination)
    print(f"Move disk{n} from {source} to {destination}") 
    towe_of_hanoi(n-1,destination,source,auxiliary)

<<<<<<< HEAD:competitive Programing-chatGpt/recurision/tower_of_hanoi.py
=======
"""
    Solves the Tower of Hanoi problem recursively.
    
    Args:
        n (int): The number of disks.
        source (str): The name of the source peg.
        auxiliary (str): The name of the auxiliary peg.
        destination (str): The name of the destination peg.
"""

def towe_of_hanoi(n,source,auxiliary,destination):
    if n==1:
        print( f"Move disk 1 from {source} to {destination}")
        return 
    
    towe_of_hanoi(n-1,source,auxiliary,destination)
    print(f"Move disk{n} from {source} to {destination}") 
    towe_of_hanoi(n-1,destination,source,auxiliary)

>>>>>>> c4f5223ba10d71953b90e01d93359193ccea7503
=======
>>>>>>> b1e894c8f4f88706e4e6472a63308c77b347ce99:Competitive_programing/recurision/tower_of_hanoi.py
print(towe_of_hanoi(45,"A","B","C"))