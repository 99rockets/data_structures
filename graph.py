#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, idx):
        return self.edges[idx]


if __name__ == '__main__':
    g = SimpleGraph()
    g.edges = {
        'A': ['B'],
        'B': ['A', 'C', 'D'],
        'C': ['A'],
        'D': ['E', 'A'],
        'E': ['B']
    }
