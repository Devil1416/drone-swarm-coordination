import random
def run():
    print('module: drone-swarm-coordination')
    data = [random.random() for _ in range(10)]
    print('avg:', sum(data)/len(data))
