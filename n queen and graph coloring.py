N = 8

# ld is an array where its indices indicate row-col+N-1
ld = [0] * 30

# rd is an array where its indices indicate row+col
rd = [0] * 30

# Column array where its indices indicate column
cl = [0] * 30

# A utility function to print solution


def printSolution(board):
	for i in range(N):
		for j in range(N):
			print(" Q " if board[i][j] == 1 else " . ", end="")
		print()

# A recursive utility function to solve N Queen problem


def solveNQUtil(board, col):
	# Base case: If all queens are placed, return true
	if col >= N:
		return True

	# Consider this column and try placing this queen in all rows one by one
	for i in range(N):
		# Check if the queen can be placed on board[i][col]
		if (ld[i - col + N - 1] != 1 and rd[i + col] != 1) and cl[i] != 1:
			# Place this queen in board[i][col]
			board[i][col] = 1
			ld[i - col + N - 1] = rd[i + col] = cl[i] = 1

			# Recur to place the rest of the queens
			if solveNQUtil(board, col + 1):
				return True

			# If placing the queen in board[i][col] doesn't lead to a solution, backtrack
			board[i][col] = 0 # BACKTRACK
			ld[i - col + N - 1] = rd[i + col] = cl[i] = 0

	# If the queen cannot be placed in any row in this column col, return false
	return False

# This function solves the N Queen problem using Backtracking.
# It mainly uses solveNQUtil() to solve the problem.
# It returns false if queens cannot be placed, otherwise, 
# returns true and prints placement of queens in the form of 1s.
# Please note that there may be more than one solution; 
# this function prints one of the feasible solutions.


def solveNQ():
	board = [[0 for _ in range(N)] for _ in range(N)]

	if not solveNQUtil(board, 0):
		print("Solution does not exist")
		return False

	printSolution(board)
	return True


# Driver program to test above function
if __name__ == "__main__":
	solveNQ()


#graph coloring

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def greedy_coloring(self):
        # Initialize all vertices as unassigned
        result = [None] * self.V

        # Assign the first color to the first vertex
        result[0] = "Red"

        # List of available colors
        colors = ["Red", "Green", "Blue"]

        # Assign colors to remaining V-1 vertices
        for u in range(1, self.V):
            # A set to track unavailable colors
            available_colors = set(colors)

            # Mark colors of adjacent vertices as unavailable
            for v in self.graph[u]:
                if result[v] is not None:
                    available_colors.discard(result[v])

            # Assign the first available color
            if available_colors:
                result[u] = available_colors.pop()  # Get one available color

        # Print the result
        for u in range(self.V):
            print(f"Vertex {u} --> Color {result[u]}")

# Example usage:
if __name__ == "__main__":
    # Create a graph with 5 vertices
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    print("Graph:")
    print("V0----V2")
    print("|    / |")
    print("|   /  |  V4")
    print("|  /   | /")
    print("| /    |/")
    print("V1----V3")

    print("Coloring of vertices:")
    graph.greedy_coloring()
