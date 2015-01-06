import random
import string

def rand_string(length):
    chars = string.ascii_lowercase
    #chars = string.letters
    return ''.join([random.choice(chars) for i in range(length)])


def compare_score(string1, string2):
    score = 0
    size = len(string1)
    for i in range(size):
        if string1[i] == string2[i]:
            score += 1
    return score


def max_like(target, times):
    score = 0
    size = len(target)
    most_like = rand_string(size)
    for i in range(times):
        guess = rand_string(size)
        measure = compare_score(guess, target)
        if measure > score:
            score = measure
            most_like = guess
        if score == size:
            print "Guess exactlyr. Done."
            break
    return score*1.0/size, most_like


if __name__ == "__main__":
    size = 27
    target = rand_string(size)
    times = 1000
    score, guess = max_like(target, times)
    print target
    print guess
    print score
