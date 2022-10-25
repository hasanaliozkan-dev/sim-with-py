import numpy as np
import random
import simpy

NUMBER_OF_BOOKS = 1000
NUMBER_OF_TABLES = 250
STUDENTS_ARRIVAL_TIME = 10


class Library:
    def __init__(self, env):
        self.env = env
        self.book = simpy.Resource(env, capacity=NUMBER_OF_BOOKS)
        self.table = simpy.Resource(env, capacity=NUMBER_OF_TABLES)

    def get_book(self, student):
        yield self.env.timeout(random.randint(1, 3))

    def get_table(self, student):
        yield self.env.timeout(random.randint(1, 3))
        
