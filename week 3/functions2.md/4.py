 def a(movies):
     s = 0
     k=len(movies)
     for i in movies:
         s = s+i['imdb']
     s = s/k
     return s
 print(a(movies))