<<<<<<< HEAD
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
print(towe_of_hanoi(45,"A","B","C"))