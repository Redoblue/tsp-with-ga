import numpy as np

class Graph(object):
    def __init__(self):
        self.cities = []
        self.dists = np.zeros((34, 34), dtype=np.float16)

        self.init_cities()
        self.init_dists()


    def _dist(self, i, j):
        d_lon = self.cities[i][1] - self.cities[j][1]
        d_lat = self.cities[i][2] - self.cities[j][2]
        return np.linalg.norm((d_lon, d_lat), 2)

    def init_cities(self):
        with open('china.csv', 'r') as f:
            for line in f:
                ll = line.strip().split(';')
                self.cities.append((ll[0], float(ll[1]), float(ll[2])))

    def init_dists(self):
        for i in range(34):
            for j in range(34):
                self.dists[i, j] = self._dist(i, j)


if __name__ == '__main__':
    g = Graph()

    print(g.cities)
    print(g.dists)

