 def a(s):
   for i in movies:
     if i['name'] == s:
         if(i['imdb']> 5.5):
             print('True')
         else:
             print('False')
 s = input()
 a(s)