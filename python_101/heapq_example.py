from pprint import pprint 
import heapq 

map = """\
.......X..
.......X..
....XXXX..
..........
..........
"""


def parse_map(map):
    lines = map.splitlines() 
    origin = 0,0
    destination = len(lines[-1])-1, len(lines)-1 
    return lines, origin, destination 


def is_valid(lines, position):
    x, y = position
    if not (0 <= y < len(lines) and 0 <=x < len(lines[y])): return False 
    
    if lines[y][x] == 'X': return False 

    return True 

def get_neighbors(lines, current): 
    x, y = current 

    for dx in [-1, 0, 1]: 
        for dy in [-1, 0, 1]:
            if dx==0 and dy==0:
                continue 
            position = dx+x, dy+y
            if is_valid(lines, position): 
                yield position 


def get_shorter_paths(tentative, positions, through):
    path = tentative[through] + [through] 
    for position in positions: 
        if position in tentative and len(tentative[position]) <= len(path):
            continue 
        yield position, path 


def draw_path(lines, result):
    print(result)

    for i in range(len(lines)): 
        lines[i] = list(lines[i])
    for x,y in result: 
        lines[y][x] = 'P'
    pprint(lines)



def find_path(map):
    lines, origin, destination = parse_map(map) 

    print(lines) 
    print(origin)
    print(destination) 

    tentative = {origin: []}
    candidates = [(0, origin)]
    certain = set()

    while destination not in certain and len(candidates) > 0: 
        _ignored, current = heapq.heappop(candidates)
        if current in certain: 
            continue 
        certain.add(current) 
        print('certain set(): ')
        pprint(certain)

        neighbors = set(get_neighbors(lines, current)) - certain 

        print('printing neighbors') 
        pprint(neighbors) 

        shorter = get_shorter_paths(tentative, neighbors, current)
        for neighbor, path in shorter: 
            print("printing tentative") 
            
            pprint(tentative) 

            tentative[neighbor] = path 
            heapq.heappush(candidates, (len(path), neighbor)) 

    if destination in tentative: 
        output = tentative[destination] + [destination] 
        draw_path(lines, output) 
        return output 
    else: 
        raise ValueError("no pah exists") 


result = find_path(map) 

pprint(result)





