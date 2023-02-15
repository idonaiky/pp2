def a(movies):
    b = input()
    lst=[]
    for i in movies:
        c=i['category']
        if b.lower()==c.lower():
            lst.append(i)
    return lst
print(a(movies))