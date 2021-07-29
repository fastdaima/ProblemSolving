class Solution:
    def maxConnected(self,grid):
        maxCount = 0
        seen = {}
        for y in range(0,len(grid)):
            for x in range(0,len(grid[y])):
                count = self.__traverse(grid, x, y)
                maxCount = max(count,maxCount)
        return maxCount

    def __traverse(self,grid,x,y):
        return self.__traverseHelper(grid, x, y, 0, {})

    # recursive function 
    def __traverseHelper(self, grid, x, y, count, seen):
        key = "%s,%s" % (x,y)
        if seen.get(key) != None:
            return 0
        seen[key] = True

        color = grid[y][x]
        neighbors = self.__getNeighbors(grid, x, y)
        sum = 1
        for point in neighbors:
            i = point[0]
            j = point[1]
            if grid[j][i] != color:
                continue
            seen[key]=True
            sum += self.__traverseHelper(grid,i,j,1,seen)
        return sum 

    # iterative function
    def __traverseHelperIterative(self, grid, x, y, count, seen):
        color = grid[y][x]
        sum = 0
        stack = []
        stack.append([x,y])
        
        while len(stack)>0:
            p = stack.pop()
            item_x = p[0]
            item_y = p[1]

            key = "%s,%s" % (item_x,item_y)
            if seen.get(key) != None:
                continue
            if grid[item_y][item_x] != color:
                continue

            seen[key] = True
            sum = sum + 1
            neighbors = self.__getNeighbors(grid, item_x, item_y)
            for point in neighbors:
                i = point[0]
                j = point[1]
                stack.append([i,j])
        return sum 


    def __getNeighbors(self,grid,x,y):
        coords = []
        neighbors = [
            [-1,0],
            [0,-1],
            [1,0],
            [0,1],
        ]

        for n in neighbors:
            coordX = x + n[0]
            coordY = x + n[1]
            if coordX < 0 or coordY < 0 or coordX >= len(grid[0]) or coordY >= len(grid):
                continue
            coords.append([coordX,coordY])
        return coords

s = Solution()
grid = [
    ['b','r','g'],
    ['b','g','r'],
    ['b','b','b'],
]
sum = 0
print (s.maxConnected(grid))





