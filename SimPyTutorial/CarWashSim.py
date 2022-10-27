import random
import simpy

RANDOM_SEED = 42
NUM_MACHINES = 4  
WASHTIME = 5      
T_INTER = 7       
SIM_TIME = 120     

class Carwash(object):
    def __init__(self, env, num_machines, washtime):
        self.env = env
        self.machine = simpy.Resource(env, num_machines)
        self.washtime = washtime

    def wash(self, car):
        yield self.env.timeout(WASHTIME)
        print("Carwash removed %d%% of %s's dirt." %
              (random.randint(50, 99), car))

def car(env, name, cw):
    print('%s arrives at the carwash at %.2f.' % (name, env.now))
    
    with cw.machine.request() as request:
        yield request

        print('%s enters the carwash at %.2f.' % (name, env.now))
        yield env.process(cw.wash(name))

        print('%s leaves the carwash at %.2f.' % (name, env.now))

def setup(env, num_machines, washtime, t_inter):
    carwash = Carwash(env, num_machines, washtime)

    for i in range(4):
        env.process(car(env, 'Car %d' % i, carwash))

    while True:
        yield env.timeout(random.randint(t_inter - 1, t_inter + 1))
        i += 1
        env.process(car(env, 'Car %d' % i, carwash))

print('Carwash')
random.seed(RANDOM_SEED)  

env = simpy.Environment()
env.process(setup(env, NUM_MACHINES, WASHTIME, T_INTER))

env.run(until=SIM_TIME)