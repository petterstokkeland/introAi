# The A* algorithm
# 1. Calculate the manhatten distanse from the start og goal position
# list_open: {node, f-value}, will only contains the node that's is nighbour with the last node visted
# list_Active When the node is [{node-name, f, g, h, last}]
# h(n) absolute distance, manhatten or ecliuds distance
# g(n) shortest distance currently found
# f(n) = g(n) + h(n)



#importing the class Map_obj


#pousdo code: 
# def all variable
# need to calculate the h score, if not we just need to make a guess
# set all f, g and h to inf except starting posistion
# find all nighbours and update the g score if that value is smaller then old value
# if that is true, update wich node we came from. 
# then update the f score, witch will be the sum of g and h score. 

# this was one iteration 
# now we ca load the next node {name, f-value} with the smalles f-value

"""
Helper class to controll the queue and priority
it will bring you the item with the lowest "cost"

"""
# class PriorityQueue:
   
#     def __init__(self):
#         self.elements : list[tuple[float, T]]= []
#     def emty(self) -> bool:
#         return not self.elements
#     def put(self, item: T, priority: float):
#         heapq.heappush(self.elements, (priority, item))
#     def get(self) -> T:
#         return heapq.heappop(self.elements)[1]
    

"""
Calculate the manhatten distance
"""
import Map
import heapq
class Astar():

    def __init__(self, task:int)-> None :
        self.theMap = Map.Map_Obj(task)
        self.frontier = []
    """
    Heuristic method to calculate the distance between to coordinates
    """
    def manhatten(self, a: list[int,int], b: list[int,int]) -> float:   
        x1, y1 = a[0], a[1]
        x2, y2 = b[0], b[1]
        return abs(x1-x2) + abs(y1-y2)
    """
    Methods that takes a coordinate x and y and find all neighbors that are walkable
    returns a list with coordinates [x,y]
    """
    def neighbors(self, x: int, y: int ) -> list[list[int,int]]:
        coordinate: list[list[int,int]] = []
        if(self.theMap.get_cell_value([x,y+1]) != -1):
            coordinate.append([x, y+1])
        if(self.theMap.get_cell_value([x+1,y]) != -1):
            coordinate.append([x+1, y])
        if(self.theMap.get_cell_value([x,y-1]) != -1):
            coordinate.append([x, y-1])
        if(self.theMap.get_cell_value([x-1,y]) != -1):
            coordinate.append([x-1, y])
        return coordinate
    
    """
    
    """
    def a_star(self) -> tuple:
        """
        Defining the start position and goal position
        """
        start: list[int,int] = self.theMap.get_start_pos()
        goal: list[int,int] = self.theMap.get_end_goal_pos()

        """
        Heap provide a tree where the root always the minimal value
        (0,start) indicate that 0 is the values used to ordering and start data
        associated with the value
        """
        heapq.heappush(self.frontier, (0,start))
    
        """
        - came_from is a dictionary that will keep track of where each node came from 
        (which node it was explored from). This will be useful to backtrack the path 
        from the goal to the start.
        - cost_so_far is a dictionary that keeps track of the cost to reach each node 
        from the start node.
        Both dictionaries are initialized with the starting position. 
        The starting position has no previous node (hence None in came_from), and its cost is 0.
        """
        came_from: dict[tuple(int,int), tuple(int,int)] = {}
        cost_so_far: dict[tuple(int,int), float] = {}
        came_from[tuple(start)] = None
        cost_so_far[tuple(start)] = 0
        
        """
        loop as long there are nodes in frontier
        """
        while len(self.frontier) > 0:
            """
            current will be the node with the lowest value 
            and the node that will be explored
            """
            current: list[int,int] = heapq.heappop(self.frontier)[1]
            """
            break state if goal is found
            """
            if current == goal:
                print('found goal')
                break
            
            """
            - next will be the next node, and will use neighbors to check all next steps
            - new cost will be the dict with the new cost for each node from current position
            + the new value for moving to the neighbor
            - if the node haven't been explored or the "new" path is cheaper than the current path
            the dict and frontier will be updated
            - The priority will be the cost to reach the node + the huristic (manhatten) value
            the node is added to the frontier with the value and the "next" node value and
            the came from is updated with the new neightbor and value "tuple(current)
            """
            for next in self.neighbors(current[0], current[1]):
                new_cost = cost_so_far[tuple(current)] + self.theMap.get_cell_value(next)
                if tuple(next) not in cost_so_far or new_cost < cost_so_far[tuple(next)]:
                    cost_so_far[tuple(next)] = new_cost
                    priority = new_cost + self.manhatten(next, goal)
                    heapq.heappush(self.frontier, (priority,next))
                    came_from[tuple(next)] = tuple(current)
    
        return came_from
    

"task 1"

# map_obj = Map.Map_Obj(1)
# map_obj.show_map()
# A_stjerne = Astar(1)
# came_from = A_stjerne.a_star()
# temp_pos = list(came_from[tuple(map_obj.get_goal_pos())])
# while temp_pos != map_obj.get_start_pos():
#     map_obj.replace_map_values(temp_pos, 5, map_obj.get_goal_pos())
#     temp_pos = list(came_from[tuple(temp_pos)])
# map_obj.show_map()

"task 2"

# map_obj = Map.Map_Obj(4)
# map_obj.show_map()
# A_stjerne = Astar(4)
# came_from = A_stjerne.a_star()
# temp_pos = list(came_from[tuple(map_obj.get_goal_pos())])
# while temp_pos != map_obj.get_start_pos():
#     map_obj.replace_map_values(temp_pos, 5, map_obj.get_goal_pos())
#     temp_pos = list(came_from[tuple(temp_pos)])
# map_obj.show_map()

"""
    Variabler: 
    liste med alle stedene på samfundet
    liste med 
    
    red blob games
"""
      

