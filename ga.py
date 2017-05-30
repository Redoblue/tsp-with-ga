import random
from life import Life


class GA(object):
    def __init__(self,
                 rate_cross,
                 rate_mutate,
                 num_life,
                 len_gene,
                 fun_fitness=lambda x: 1):
        self.rate_cross = rate_cross
        self.rate_mutate = rate_mutate
        self.num_life = num_life
        self.len_gene = len_gene
        self.fun_fitness = fun_fitness

        self.lives = []
        self.best = None
        self.generation = 1
        self.count_cross = 0
        self.count_mutate = 0
        self.bounds = 0.0

        self.init_population()

    def init_population(self):
        self.lives = []

        for _ in range(self.num_life):
            gene = [x for x in range(self.len_gene)]
            random.shuffle(gene)
            life = Life(gene)
            self.lives.append(life)

    def judge(self):
        self.bounds = 0.0
        self.best = self.lives[0]
        for life in self.lives:
            life.score = self.fun_fitness(life)
            self.bounds += life.score

            if life.score > self.best.score:
                self.best = life

    def cross(self, p1, p2):
        i = random.randint(0, self.len_gene - 1)
        j = random.randint(i, self.len_gene - 1)

        gene_to_cross = p2.gene[i:j]
        new_gene = []
        len1 = 0
        for g in p1.gene:
            if len1 == i:
                new_gene.extend(gene_to_cross)
                len1 += 1
            if g not in gene_to_cross:
                new_gene.append(g)
                len1 += 1
        self.count_cross += 1

        return new_gene

    def mutate(self, gene):
        i = random.randint(0, self.len_gene - 1)
        j = random.randint(0, self.len_gene - 1)

        new_gene = gene[:]
        new_gene[i], new_gene[j] = new_gene[j], new_gene[i]
        self.count_mutate += 1

        return new_gene

    def get_one(self):
        r = random.uniform(0, self.bounds)
        for life in self.lives:
            r -= life.score
            if r <= 0:
                return life

        raise Exception("wrong selection", self.bounds)

    def new_child(self):
        p1 = self.get_one()
        rate = random.random()

        if rate < self.rate_cross:
            p2 = self.get_one()
            gene = self.cross(p1, p2)
        else:
            gene = p1.gene

        rate = random.random()
        if rate < self.rate_mutate:
            gene = self.mutate(gene)

        return Life(gene)

    def next(self):
        self.judge()
        new_lives = []
        new_lives.append(self.best)

        while len(new_lives) < self.num_life:
            new_lives.append(self.new_child())
        self.lives = new_lives
        self.generation += 1
