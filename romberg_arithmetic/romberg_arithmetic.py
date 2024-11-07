import math


def romberg_arithmetic(f, a, b, wrong_number):
    T = [((b - a) / 2) * (f(a) + f(b))]
    k = 1
    while True:
        sum = 0
        for i in range(1, 2 ** (k - 1) + 1):
            sum = sum + f(a + ((2 * i - 1) * (b - a)) / (2 ** k))
        T.append((T[k - 1] / 2) + ((b - a) * sum) / (2 ** k))
        if T[k] - T[k - 1] < (3 * wrong_number):
            break
        k = k + 1
    return 2 ** k


def function(x):
    if x == 0:
        return 1
    else:
        return math.sin(x) / x


if __name__ == "__main__":
    result = romberg_arithmetic(function, 0, 1, 0.5 * 10 ** -6)
    print(result)
