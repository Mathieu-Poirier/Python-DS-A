Depth-First-Search is an algorithm useful for optimizing for a certain criteria, pathfinding and scheduling tasks in the most efficient manner

Overview:

Stack-based DFS + Hash Table:

Stack: [start_pos]
Predecessors: {start_pos: None}

pop the stack
we ask the program if we reached our goal
if so we are done running the algorithm
otherwise push undiscovered neighbors onto the stack and add them to the predecessors table (cardinal directions)
repeat if there are items on the stack


and then we can use backtracking to find the path with the hash table 