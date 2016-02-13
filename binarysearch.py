# Binary Seacr Array

from time import time

def contains(collections, target):
    """ determines wheteher collection contains target """
    return target in collections


def bs_contains(ordered, target):
    """ Use binary search array to find if target is there in collections """
    low =0
    high = len(ordered) -1
    while low <= high:
        mid = (low+high)//2
        if target == ordered[mid]:
            return True
        elif target < ordered[mid]:
            high = mid -1 
        else : 
            low = mid + 1      
     
    return False           




def performance():
    """Determines execution performance of contains """
    n = 1024
    while(n < 50000000):
        sorted = range(n)
        now = time()

        # Code whoose performance is to be evaluated

        bs_contains(sorted , -1)
        done = time()
        print(n, ((done - now)*10000000))
        n *= 2




def main():
    performance()

if __name__ == "__main__": main()