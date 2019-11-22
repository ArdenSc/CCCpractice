def is_prime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True


def find_prime_divisors(n):
    out = []
    for i in range(2, n):
        if is_prime(i) and is_prime(n - i):
            if any(str(i) in pair for pair in out):
                break
            out.append([str(i), str(n - i)])
    return " ".join([" ".join(pair) for pair in out]) if out != [] else False


with open("inputS2.txt", 'r') as data:
    for lineNum, line in enumerate(data):
        line = line.strip()
        if lineNum == 0:
            continue
        print(find_prime_divisors(int(line)*2))
