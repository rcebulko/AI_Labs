# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = False

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = False

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = True

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = True

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = True

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = False

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.

def bfs(graph, start, goal):
    """Find a path in a graph using breadth-first search.

    Args:
        graph (Graph): A graph to search.
        start (str): A node from which to start the search.
        goal (str): A node to search for.

    Returns:
        list of str: A list of node names defining a path or, if no path is
            found, an empty list.
    """

    final = []
    agenda = [[start]]

    # Process node queue
    while agenda:
        path = agenda.pop(0)

        # Exit if a path is found which reaches the goal
        if path[-1] == goal:
            final = path
            break

        # Push the new paths onto the queue
        connected = graph.get_connected_nodes(path[-1])
        for node in connected:
            # Ignore previously visited nodes
            if node not in path:
                agenda.append(path + [node])

    # Return the final path or initial empty list
    return final

## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def dfs(graph, start, goal):
    """Find a path in a graph using depth-first search.

    Args:
        graph (Graph): A graph to search.
        start (str): A node from which to start the search.
        goal (str): A node to search for.

    Returns:
        list of str: A list of node names defining a path or, if no path is
            found, an empty list.
    """

    final = []
    agenda = [[start]]

    # Process node stack
    while agenda:
        path = agenda.pop()

        # Exit if a path is found which reaches the goal
        if path[-1] == goal:
            final = path
            break

        # Push the new paths onto the stack
        connected = graph.get_connected_nodes(path[-1])
        for node in connected:
            # Ignore previously visited nodes
            if node not in path:
                agenda.append(path + [node])

    # Return the final path or initial empty list
    return final

## Now we're going to add some heuristics into the search.
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
def hill_climbing(graph, start, goal):
    """Find a path in a graph using hill-climbing or heuristic-based search.

    Notes:
        At each step, the algorithm extends the path which is estimated to be
        closest to the goal.

    Args:
        graph (Graph): A graph to search.
        start (str): A node from which to start the search.
        goal (str): A node to search for.

    Returns:
        list of str: A list of node names defining a path or, if no path is
            found, an empty list.
    """

    final = []
    agenda = [[start]]

    # Process node stack
    while agenda:
        path = agenda.pop()

        # Exit if a path is found which reaches the goal
        if path[-1] == goal:
            final = path
            break

        # Push the new paths onto the stack in order of heuristic value on top
        connected = graph.get_connected_nodes(path[-1])
        for node in sorted(
                connected,
                reverse=True,
                key=lambda n: graph.get_heuristic(n, goal)
            ):
            # Ignore previously visited nodes
            if node not in path:
                agenda.append(path + [node])

    # Return the final path or initial empty list
    return final

## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the
## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):
    """Find a path in a graph using hill-climbing or heuristic-based search.

    Notes:
        At each step, the algorithm selects the set of paths which are estimated
        to be the closest and discards all others.

    Args:
        graph (Graph): A graph to search.
        start (str): A node from which to start the search.
        goal (str): A node to search for.
        beam_width (int): The maximum number of paths to explore at each step in
            the search.

    Returns:
        list of str: A list of node names defining a path or, if no path is
            found, an empty list.
    """

    final = []
    next_level = [[start]]

    # Process node list
    while next_level:
        # Sort nodes by heuristic and take the best ones
        curr_level = sorted(
            next_level,
            reverse=True,
            key=lambda p: graph.get_heuristic(p[-1], goal)
        )[-beam_width:]
        next_level = []

        # Process node list
        while curr_level:
            path = curr_level.pop()

            # Exit if a path is found which reaches the goal
            if path[-1] == goal:
                final = path
                break

            # Push the new paths onto the list
            connected = graph.get_connected_nodes(path[-1])
            for node in connected:
                # Ignore previously visited nodes
                if node not in path:
                    next_level.append(path + [node])
        else:
            # If a path hasn't been found at the current level, search the next
            # level
            continue
        break

    # Return the final path or initial empty list
    return final

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    """Find the length of a path.

    Args:
        graph (Graph): A graph to search.
        node_names (list of str): A list of node names representing a path

    Returns:
        int: The sum of the weights of all edges in the path.
    """

    total = 0
    for i in range(0, len(node_names) - 1):
        total += graph.get_edge(node_names[i], node_names[i + 1]).length

    return total

def branch_and_bound(graph, start, goal):
    """Find a path in a graph using branch-and-bound search.

    Notes:
        At each step, the algorithm extends the path which is estimated to be
        the shortest path based on its length so far and its estimated distance
        to the goal.

    Args:
        graph (Graph): A graph to search.
        start (str): A node from which to start the search.
        goal (str): A node to search for.

    Returns:
        list of str: A list of node names defining a path or, if no path is
            found, an empty list.
    """

    final = []
    agenda = [[start]]

    # Process node list
    while agenda:
        path = agenda.pop(0)

        # Exit if a path is found which reaches the goal
        if path[-1] == goal:
            final = path
            break

        # Push the new paths onto the list
        connected = graph.get_connected_nodes(path[-1])
        for node in connected:
            # Ignore previously visited nodes
            if node not in path:
                agenda.append(path + [node])

        # Sort potential paths by path length
        agenda.sort(key=lambda p: path_length(graph, p))

    # Return the final path or initial empty list
    return final

def a_star(graph, start, goal):
    """Find a path in a graph using A* search.

    Notes:
        At each step, the algorithm extends the path which is estimated to be
        the shortest path based on its length so far and its estimated distance
        to the goal. It tracks the nodes which have already been extended since
        it is known the path is already shortest.

    Args:
        graph (Graph): A graph to search.
        start (str): A node from which to start the search.
        goal (str): A node to search for.

    Returns:
        list of str: A list of node names defining a path or, if no path is
            found, an empty list.
    """
    final = []
    agenda = [[start]]
    extended = set()

    # Process node list
    while agenda:
        path = agenda.pop(0)

        # Exit if a path is found which reaches the goal
        if path[-1] == goal:
            final = path
            break
        # Skip paths to nodes which are known to be sub-optimal
        elif path[-1] in extended:
            continue

        # Push the new paths onto the list
        connected = graph.get_connected_nodes(path[-1])
        for node in connected:
            # Ignore previously visited nodes
            if node not in path:
                agenda.append(path + [node])

        # Update the extended set
        extended.add(path[-1])
        # # Sort potential paths by expected total path length
        agenda.sort(
            key=lambda p:
            graph.get_heuristic(p[-1], goal) + path_length(graph, p)
        )

    # Return the final path or initial empty list
    return final


## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):
    """Determine the admisssibility of a graph.

    Args:
        graph (Graph): A graph to test.
        goal (str): A node to target.

    Returns:
        bool: Whether or not the heuristic value is at most the shortest path
            length between the goal and any other point on the graph.
    """

    admissible = True

    for node in graph.nodes:
        admissible &= graph.get_heuristic(node, goal) <= \
            path_length(graph, a_star(graph, node, goal))

        if not admissible:
            break

    return admissible

def is_consistent(graph, goal):
    """Determine the consistency of a graph.

    Args:
        graph (Graph): A graph to test.
        goal (str): A node to target.

    Returns:
        bool: Whether or not the length of any edge and the heuristic values to
            each point of the edges form a valid triangle.
    """

    consistent = True

    for edge in graph.edges:
        consistent &= edge.length >= abs(
            graph.get_heuristic(edge.node1, goal) -
            graph.get_heuristic(edge.node2, goal)
        )

        if not consistent:
            break

    return consistent

HOW_MANY_HOURS_THIS_PSET_TOOK = 3
WHAT_I_FOUND_INTERESTING = "How similar the various implementations are, with such minor differences"
WHAT_I_FOUND_BORING = "I was not a fan of having to worry about lexcographical ordering of nodes and order of sort operations; I later realized this didn't actually matter"
