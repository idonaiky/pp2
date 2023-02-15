def a(movies):
    lst=[]
    for i in range(0,len(movies)):
        m=movies[i]
        if m['imdb']>5.5:
            lst.append(m)
    return lst
print(a(movies)