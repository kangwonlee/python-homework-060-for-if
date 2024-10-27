import random

import exercise

random.seed()

def main():
    a = random.randint(1, 5)
    b = random.randint(6, 10)
    
    odd_sum = exercise.for_with_if(a, b, 1)
    even_sum = exercise.for_with_if(a, b, 0)

    print(f"Sum of odd numbers between {a} and {b} is {odd_sum}")
    print(f"Sum of even numbers between {a} and {b} is {even_sum}")


if "__main__" == __name__:
    main()
