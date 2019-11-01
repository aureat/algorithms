from priority_queue import PriorityQueue

def heuristic(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)

""" Greedy Best first Search """
def heuristic_search(G, s, g):
    Q = PriorityQueue()
    Q.put(s,0)
    came_from = {}
    came_from[s] = None
    while Q:
        v = Q.getMin()
        if v is g:
            break
        for i in G[v]:
            if i not in came_from:
                priority = heuristic(g, i)
                Q.put(i, priority)
                came_from[i] = v
    return came_from

""" A* Search """
def a_star(G, s, g):
    Q = PriorityQueue()
    Q.put(s,0)
    came_from = {}
    came_from[s] = None
    cost_so_far = {}
    cost_so_far[s] = 0
    while Q:
        v = Q.getMin()
        if v == g:
            break
        for i in G[v]:
            cost = cost_so_far[v] + g.cost
            if i not in came_from:
                priority = heuristic(g, i)
                Q.put(i, priority)
                came_from[i] = v
    return came_from

frontier = PriorityQueue()
frontier.put(start, 0)
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far[start] = 0

while not frontier.empty():
   current = frontier.get()

   if current == goal:
      break

   for next in graph.neighbors(current):
      new_cost = cost_so_far[current] + graph.cost(current, next)
      if next not in cost_so_far or new_cost < cost_so_far[next]:
         cost_so_far[next] = new_cost
         priority = new_cost + heuristic(goal, next)
         frontier.put(next, priority)
         came_from[next] = current

# g = Graph(6)
# g.add_edge(1,2)
# g.add_edge(1,3)
# g.add_edge(2,4)
# g.add_edge(1,5)
# g.add_edge(5,6)
#
# heuristic_search(g, start, goal)

# def a_star():
#     open_list = [Node(0,0)]
#     closed_list = []
#     while open_list:
#         min = 0
#         for i in open_list:
#             if i.f < min:
#                 upd= i
#                 min = i.f
#             open(list)
