# -*- coding: utf-8 -*-

import random
from Life import Life

class GA(object):
      def __init__(self, cross_rate, mutation_rate, life_count, gene_length, match_fun=lambda life : 1):
            self.croessRate = cross_rate
            self.mutationRate = mutation_rate
            self.lifeCount = life_count
            self.geneLenght = gene_length
            self.matchFun = match_fun                 # 适配函数
            self.lives = []                           # 种群
            self.best = None                          # 保存这一代中最好的个体
            self.generation = 1
            self.crossCount = 0
            self.mutationCount = 0
            self.bounds = 0.0                         # 适配值之和，用于选择是计算概率

            self.init_population()


      def init_population(self):
            self.lives = []
            for i in range(self.lifeCount):
                  gene = [ x for x in range(self.geneLenght)]
                  random.shuffle(gene)
                  life = Life(gene)
                  self.lives.append(life)


      def judge(self):
            self.bounds = 0.0
            self.best = self.lives[0]
            for life in self.lives:
                  life.score = self.matchFun(life)
                  self.bounds += life.score
                  if self.best.score < life.score:
                        self.best = life


      def cross(self, parent1, parent2):
            index1 = random.randint(0, self.geneLenght - 1)
            index2 = random.randint(index1, self.geneLenght - 1)
            tempGene = parent2.gene[index1:index2]   # 交叉的基因片段
            newGene = []
            p1len = 0
            for g in parent1.gene:
                  if p1len == index1:
                        newGene.extend(tempGene)     # 插入基因片段
                        p1len += 1
                  if g not in tempGene:
                        newGene.append(g)
                        p1len += 1
            self.crossCount += 1
            return newGene


      def  mutate(self, gene):
            index1 = random.randint(0, self.geneLenght - 1)
            index2 = random.randint(0, self.geneLenght - 1)

            newGene = gene[:]       # 产生一个新的基因序列，以免变异的时候影响父种群
            newGene[index1], newGene[index2] = newGene[index2], newGene[index1]
            self.mutationCount += 1
            return newGene


      def get_one(self):
            r = random.uniform(0, self.bounds)
            for life in self.lives:
                  r -= life.score
                  if r <= 0:
                        return life

            raise Exception("选择错误", self.bounds)


      def new_child(self):
            parent1 = self.get_one()
            rate = random.random()

            # 按概率交叉
            if rate < self.croessRate:
                  # 交叉
                  parent2 = self.get_one()
                  gene = self.cross(parent1, parent2)
            else:
                  gene = parent1.gene

            # 按概率突变
            rate = random.random()
            if rate < self.mutationRate:
                  gene = self.mutate(gene)

            return Life(gene)


      def next(self):
            self.judge()
            new_lives = []
            new_lives.append(self.best)            #把最好的个体加入下一代

            while len(newLives) < self.lifeCount:
                  new_lives.append(self.new_child())
            self.lives = new_lives
            self.generation += 1

