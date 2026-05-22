cap1 = 4
cap2 = 3
target = 2
visited = set()
def dfs(jug1, jug2):

    if (jug1,jug2) in  visited:
        return False

    print(f"({jug1} , {jug2})")
    if jug1 == target or  jug2 == target:
        return True


    visited.add((jug1,jug2))

    return (
        dfs(0,jug2) or
        dfs(jug1, 0) or
        dfs(cap1,jug2) or
        dfs(jug1, cap2) or 
        dfs(max(0,jug1 - (cap2 - jug2)),min(cap2, jug1+jug2)) or
        dfs(min(jug1+jug2, cap1), max(jug2 - (cap1 - jug1),0))
    )

dfs(0,0)