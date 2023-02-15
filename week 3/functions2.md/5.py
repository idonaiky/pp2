def a(movies, category):
    s = 0
    n = 0
    for movie in movies:
        if movie['category'] == category:
            s += movie['imdb']
            n += 1
    return s / n

print(a(movies, 'Suspense'))