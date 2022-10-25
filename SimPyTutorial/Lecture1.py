import simpy
"""
def generator(n):
    while True:
        for i in range(n):
            yield i


def function(n):
    for i in range(n):
        return i
"""

def main():
    env = simpy.Environment()
    env.process(traffic_light(env))
    env.run(until=120)
    print("Simulation Complete")

def traffic_light(env):
    while True:
        print('Light turns green at t= %d' % env.now)
        yield env.timeout(30)
        print('Light turns yellow at t= %d' % env.now)
        yield env.timeout(5)
        print('Light turns red at t= %d' % env.now)
        yield env.timeout(20)


if __name__ == '__main__':
    main()
 