import sys

class RoundMas:
    def __init__(self, n):
        self.n = int(n)

    def move_around(self, m):
        current = 1
        route = []
        while True:
            route.append(current)
            current = (current - 1 + int(m) - 1) % self.n + 1
            if current==1:
                break
        return ''.join(map(str, route))

r1=RoundMas(sys.argv[1])
route1=r1.move_around(sys.argv[2])
r2=RoundMas(sys.argv[3])
route2=r2.move_around(sys.argv[4])
print(route1+route2)