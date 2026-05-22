from  queue import PriorityQueue

initail  = (3,3,0)
goal = (0,0,1)

def h(state):
    a, b, c = state
    return a+b

def valid(state):
    m, c, b = state
    if m > 3  or  c > 3 or  m < 0 or  c <0:
        return False
    if m < c and m > 0:
        return False
    if 3-m < 3-c and 3-m > 0:
        return False
    return True


def generate(state):
    mleft, cleft, boat = state
    generated = []
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    for dm, dc in moves:
        if boat == 0:
            m = mleft - dm
            c = cleft - dc
            b = 1
        else:
            b = 0
            m = mleft + dm
            c = cleft + dc

        if valid((m,c,b)):
            generated.append((m,c,b))

    return generated
   


def a_star():
    pq = PriorityQueue()
    pq.put((h(initail),0,initail,[initail]))
    visited = set()
    while not pq.empty():
        f, g, current, path = pq.get()
        if current in  visited:
            continue
        visited.add(current)
        print(current)
        if current == goal:
            for i in path:
                print(i)
            print(current)
            return

        moves = generate(current)
        new_g = g+1
        for move in moves:
            if move not in visited:
                pq.put((h(move)+new_g,new_g,move,path+[move]))

a_star()
