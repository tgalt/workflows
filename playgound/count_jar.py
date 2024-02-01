# Python loop to count money in a jar

def counter(jar):
    total = 0
    for coin in jar:
        total += coin
    return total