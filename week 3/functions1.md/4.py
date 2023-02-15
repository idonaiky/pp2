 def is_prime(n):
     if n < 2:
         return False
     for i in range(2, int(n**0.5) + 1):
         if n % i == 0:
             return False
     return True
 def filter_prime(lst):
     return [x for x in lst if is_prime(x)]
 line = input("Enter a list of numbers separated by spaces: ")
 words = line.split(' ')
 numbers = [int(i) for i in words]
 print(filter_prime(numbers))
