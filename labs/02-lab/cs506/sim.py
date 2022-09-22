import math


def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)


def manhattan_dist(x, y):
    return sum(abs(x-y) for x, y in zip(x, y))

    #raise NotImplementedError()


def jaccard_dist(x, y):
    intersection = len(list(set(x).intersection(y)))
    union = (len(x) + len(y)) - intersection
    jaccard_sim = float(intersection)/union
    ans = 1 - jaccard_sim
    return ans
    #raise NotImplementedError()


def cosine_sim(x, y):
    # Similarity = (A.B) / (||A||.||B||)

    dot = sum([ix*iy for (ix, iy) in zip(x, y)])
    normX = math.sqrt(sum(pow(element, 2) for element in x))
    normY = math.sqrt(sum(pow(element, 2) for element in y))

    dotDenom = sum([vx*vy] for (vx, vy) in zip(normX, normY))
    cosine_simil = dot / dotDenom
    return cosine_simil
    #raise NotImplementedError()

# Feel free to add more
