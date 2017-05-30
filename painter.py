import matplotlib.pyplot as plt


class Painter:
    def __init__(self, graph):
        self.graph = graph
        self.fig = plt.figure(figsize=(11, 11))
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim([85, 130])
        self.ax.set_ylim([15, 50])
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.grid(False)

    def draw_best(self, gene):
        plt.cla()
        plt.title("Travelling Salesman Problem")
        for i in range(len(gene)):
            h = gene[i]
            t = gene[(i+1) % 34]
            x = (self.graph.cities[h][1], self.graph.cities[t][1])
            y = (self.graph.cities[h][2], self.graph.cities[t][2])
            self.ax.plot(x, y, 'ko-', linewidth=2.0)
        plt.pause(0.001)

    def show(self):
        plt.show()
