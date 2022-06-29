import itertools
import ipaddress


# Задача №1

def domain_name(url: str) -> str:
    domain = url.split('//')[-1].split('www.')[-1].split('.')[0]
    return domain


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"


# Задача №2


def int32_to_ip(int32: int) -> str:
    return str(ipaddress.IPv4Address(int32))


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"


# Задача №3

def zeros(n: int) -> int:
    zeroes = 0

    while n > 0:
        n //= 5
        zeroes += n

    return zeroes


assert zeros(30) == 7
assert zeros(100) == 24
assert zeros(1000) == 249


# Задача №4


def bananas(s: str) -> set:
    result = set()

    for comb in itertools.combinations(range(len(s)), len(s) - 6):
        arr = list(s)

        for i in comb:
            arr[i] = '-'

        candidate = ''.join(arr)

        if candidate.replace('-', '') == 'banana':
            result.add(candidate)

    return result


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana",
                               "bana--na", "b--anana", "banana--", "banan--a"}


# Задача №5

def count_find_num(primesL, limit):
    result = set()

    def search(i, prod):
        if prod > limit:
            return

        if i == len(primesL):
            result.add(prod)
            return

        search(i, prod * primesL[i])
        search(i + 1, prod * primesL[i])

    search(0, 1)
    return result and [len(result), max(result)] or []


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
