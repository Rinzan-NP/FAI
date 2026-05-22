N = 4
pit = [N*[False] for _ in range(N)]
wumpus = [N*[False] for _ in range(N)]
breeze = [N*[False] for _ in range(N)]
glitter = [N*[False] for _ in range(N)]
safe = [N*[False] for _ in range(N)]
stench = [N*[False] for _ in range(N)]

def get_neighbors(x, y):
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    result = []
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N:
            result.append((nx, ny))
    return result

def is_safe(x,y):
    if not breeze[x,y]:
        for nx,ny in get_neighbors(x,y):
            safe[nx,ny] = True
            pit[nx,ny] = False
    
    if not stench[x,y]:
        for nx,ny in get_neighbors(x,y):
            safe[nx,ny] = True
            wumpus[nx,ny] = False

safe[0][0] = True
breeze[0][0] = False
stench[0][0] = False

breeze[0][1] = True
glitter[3][3] = True

is_safe(0,0)
print("Safe Cells Deduced:\n")

for i in range(N):
    for j in range(N):
        if safe[i][j]:
            print(f"Cell ({i},{j}) is SAFE")

agent_x = 0
agent_y = 0

print(f"\nAgent starts at ({agent_x},{agent_y})")
for nx, ny in get_neighbors(agent_x, agent_y):
    if safe[nx][ny]:
        print(f"Moving to safe cell ({nx},{ny})")
        if glitter[nx][ny]:
            print("Gold found!")
            print("Grab gold and exit safely")
print("\nLogical Reasoning:")
if breeze[0][1]:
    print("Breeze detected at (0,1)")
    print("Possible pit in adjacent cells")
    for nx, ny in get_neighbors(0,1):
        if not safe[nx][ny]:
            print(f"Cell ({nx},{ny}) could have a pit")


