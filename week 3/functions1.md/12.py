 def list(n):

     for i in n:

         print('* '*i)

 line = input()

 words = line.split(' ')

 numbers = [int(i) for i in words]

 list(numbers)