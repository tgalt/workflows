# Python loop to count money in a jar
def counter(jar):
    total = 0
    for coin in jar:
        total += coin
    return total

jar = [1, 2, 3, 4, 5]
print(counter(jar))