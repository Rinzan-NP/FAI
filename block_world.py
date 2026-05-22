from queue import  PriorityQueue

# Initial State
initial = [
    ['D'],
    ['B', 'A'],
    ['E', 'F', 'C']
]

# Goal State
goal = [
    ['A', 'D', 'B'],
    ['E', 'F', 'C'],
    []
]

def h(state):
    count = 0
    for i in range(3):
        for j in range(len(state[i])):
            if j >= len(goal[i]) or state[i][j] != goal[i][j]:
                count += 1
    return count


def convert(state):
    x = tuple(tuple(i) for i in state)
    return x

def generate(state):
    generated = []
    for i in range(3):
        if len(state[i]) == 0:
            continue
        block = state[i][-1]
        for j in range(len(state)):
            if i == j:
                continue
            x = [s.copy() for s in  state]
            x[i].pop()
            x[j].append(block)
            generated.append(x)
    return generated


             


def bfs():
    pq = PriorityQueue()
    pq.put((h(initial),initial))
    visited = set()

    while not pq.empty():
        prio, current  =  pq.get()
        state = convert(current)
        if state in visited:
            continue
        visited.add(state)
        print(f"State {current}")
        if current == goal:
            return 

        states = generate(current)
       
        for e in states:
            if convert(e) not in visited:
                pq.put((h(e),e))

bfs()
        