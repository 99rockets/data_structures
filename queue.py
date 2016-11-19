#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import heapq
import collections


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def put(self, item):
        self.elements.append(item)

    def get(self):
        return self.elements.popleft()

    def is_empty(self):
        return len(self.elements) == 0


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def is_empty(self):
        return len(self.elements) == 0
