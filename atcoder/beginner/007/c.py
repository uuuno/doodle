r,c = map(int, input().split())
sy,sx = map(int, input().split())
gy,gx = map(int, input().split())
maze = []
for i in range(r):
    row = input()
    r_tmp = []
    for j in range(c):
        r_tmp.append(row[j])
    maze.append(r_tmp)
maze_ans = maze

def search_next(y,x,count):
    posi = []
    if maze[y-1][x] == '.': posi.append([y-1, x]); maze_ans[y-1][x] = count;
    if maze[y][x+1] == '.': posi.append([y, x+1]); maze_ans[y][x+1] = count;
    if maze[y+1][x] == '.': posi.append([y+1, x]); maze_ans[y+1][x] = count;
    if maze[y][x-1] == '.': posi.append([y, x-1]); maze_ans[y][x-1] = count;
    return posi

count = 0
maze_ans[sy-1][sx-1] = count
posi = [[sy-1, sx-1]]
while True:
    count += 1
    new_posi = []
    for p in posi:
        new_posi += search_next(p[0], p[1], count)
    posi = new_posi
    if maze_ans[gy-1][gx-1] != '.':
        print(count)
        exit()
