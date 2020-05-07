def find_nb(m):
    volume = 0
    n = 1
    
    while volume < m:
        volume += n ** 3
        n += 1
    
    return n if volume == m else -1

print(find_nb(1071225))