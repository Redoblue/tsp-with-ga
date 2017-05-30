from ga import GA
from graph import Graph
from painter import Painter


graph = Graph()

def fitness():
    return lambda life: 1.0/dist(life.gene)

def dist(order):
    dist = 0.0
    for k in range(-1, 33):
        i, j = order[k], order[k+1]
        dist += graph.dists[i, j]
    return dist


def main(epoch):
    ga = GA(rate_cross=0.7,
            rate_mutate=0.02,
            num_life=100,
            len_gene=34,
            fun_fitness=fitness())
    painter = Painter(graph)

    for _ in range(epoch):
        ga.next()
        bg = ga.best.gene
        painter.draw_best(bg)
        d = dist(bg)
        print("%d : %f" % (ga.generation, d))
    painter.show()


if __name__ == '__main__':
    main(400)
