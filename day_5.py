
class HydrothermalVenture():
    from collections import defaultdict

    def __init__(self, filename) -> None:
        self.filename = filename

    def get_input(self):
        with open(self.filename) as f:
            data = f.readlines()
        return data

    def get_points(self, p1, p2):
        points = set()
        x1, x2 = p1[0], p2[0]
        y1, y2 = p1[1], p2[1]

        if x1 != x2 and y1 != y2:
            return []

        x, y = x1, y1
        while (not x == x2) or (not y == y2):
            points.add((x, y))
            if x < x2:
                x += 1
            elif x > x2:
                x -= 1

            if y < y2:
                y += 1
            elif y > y2:
                y -= 1
        points.add((x2, y2))
        return list(points)

    def get_points_diag(self, p1, p2):
        points = set()
        x1, x2 = p1[0], p2[0]
        y1, y2 = p1[1], p2[1]

        x, y = x1, y1
        while (not x == x2) or (not y == y2):
            points.add((x, y))
            if x < x2:
                x += 1
            elif x > x2:
                x -= 1

            if y < y2:
                y += 1
            elif y > y2:
                y -= 1
        points.add((x2, y2))
        return list(points)

    def clean_point(self, p):
        return list(map(int, p.split(",")))

    def solve(self, data):

        d = self.defaultdict(int)
        for line in data:
            p1, p2 = line.split(" -> ")
            p1, p2 = self.clean_point(p1), self.clean_point(p2)
            for point in self.get_points(p1, p2):
                d[tuple(point)] += 1

        return len([d[point] for point in d if d[point] >= 2])

    def solve_diag(self, data):

        d = self.defaultdict(int)
        for line in data:
            p1, p2 = line.split(" -> ")
            p1, p2 = self.clean_point(p1), self.clean_point(p2)
            for point in self.get_points_diag(p1, p2):
                d[tuple(point)] += 1

        return len([d[point] for point in d if d[point] >= 2])


if __name__ == '__main__':

    h1 = HydrothermalVenture('input5.txt')
    result = h1.solve(h1.get_input())
    print(f'Part 1: {result}')
    result2 = h1.solve_diag(h1.get_input())
    print(f'Part 3: {result2}')
