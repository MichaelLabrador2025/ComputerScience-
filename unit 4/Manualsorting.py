#bubble sort
import random 
numbers = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]

print(numbers)
def bubblesort (n):
    for j in range(0, len(n)-1):
        for i in range(0, len(n)-1):
            if n[i] > n[i+1]:
                n[i], n[i+1] = n[i+1], n[i]
                print(n)
              
bubblesort(numbers)