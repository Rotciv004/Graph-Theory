import random
from queue import Queue
from queue import PriorityQueue
import heapq

class Functions:


    def __init__(self, repository):
        self.repository = repository

    def print_the_number_of_vertices(self):
        return self.repository.vertices_number

    def print_all_vertices(self):
        return self.repository.vertices_out

    def find_an_edge_between_two_vertices(self, vertex_1: int, vertex_2: int) -> bool:
        for index in range(0, len(self.repository.vertices_out[vertex_1])):
            if self.repository.vertices_out[vertex_1][index] == vertex_2:
                return True

        for index in range(0, len(self.repository.vertices_out[vertex_2])):
            if self.repository.vertices_out[vertex_2][index] == vertex_1:
                return True

        return False


    def find_the_in_degree_and_the_out_degree_of_a_specified_vertex(self, vertex: int):
        return len(self.repository.vertices_in[vertex]), len(self.repository.vertices_out[vertex])

    def print_all_out_edges_for_a_specified_vertex(self, vertex: int) -> list:
        return self.repository.vertices_out[vertex]

    def print_all_in_edges_for_a_specified_vertex(self, vertex: int) -> list:
        return self.repository.vertices_in[vertex]


    def modify_the_cost_of_the_edge(self, start_vertex: int, end_vertex: int, new_cost: int):
        cost_elements = ()
        elem = list(cost_elements)
        elem.append(int(start_vertex))
        elem.append(int(end_vertex))
        cost_elements = tuple(elem)

        self.repository.costs[cost_elements] = int(new_cost)


    def delete_a_specified_vertex(self, vertex: int):
        for vert in self.repository.vertices_out[vertex]:
            cost_elements = ()
            elem = list(cost_elements)
            elem.append(int(vertex))
            elem.append(int(vert))
            cost_elements = tuple(elem)

            self.repository.costs.pop(cost_elements)

            self.repository.vertices_in[vert].remove(vertex)

            self.repository.edges_number -= 1


        self. repository.vertices_out[vertex].clear()

        for vert in self.repository.vertices_in[vertex]:
            cost_elements = ()
            elem = list(cost_elements)
            elem.append(int(vert))
            elem.append(int(vertex))
            cost_elements = tuple(elem)

            self.repository.costs.pop(cost_elements)

            self.repository.vertices_out[vert].remove(vertex)

            self.repository.edges_number -= 1

        self.repository.vertices_number -= 1

    def delete_a_specified_edge(self, start_vertex: int, end_vertex: int):
        cost_elements = ()
        elem = list(cost_elements)
        elem.append(int(start_vertex))
        elem.append(int(end_vertex))
        cost_elements = tuple(elem)

        self.repository.costs.pop(cost_elements)

        self.repository.vertices_out[start_vertex].remove(end_vertex)

        self.repository.vertices_in[end_vertex].remove(start_vertex)

        self.repository.edges_number -= 1


    def random_graph(self,vertices_number:int, edges_number:int):
        self.repository.vertices_in.clear()
        self.repository.vertices_out.clear()
        self.repository.costs.clear()

        self.repository.vertices_number = vertices_number
        self.repository.edges_number = edges_number

        for vertex in range(0,self.repository.vertices_number):
            self.repository.vertices_out[vertex] = []
            self.repository.vertices_in[vertex] = []

        for _ in range(0,self.repository.edges_number):
            start_vertex = random.randint(0, self.repository.vertices_number - 1)
            end_vertex = random.randint(0, self.repository.vertices_number - 1)
            cost = random.randint(1, 100)

            self.repository.vertices_in[end_vertex].append(start_vertex)
            self.repository.vertices_out[start_vertex].append(end_vertex)
            self.repository.costs[(start_vertex, end_vertex)] = cost

    def print_the_final_points_of_a_vertex(self, start_vertex:int)->list:
        vertices_list = []

        for vertex in self.repository.vertices_out[start_vertex]:
            vertices_list.append(vertex)

        return vertices_list

    def add_a_vertex(self, vertex:int):
        self.repository.vertices_out[vertex] = []
        self.repository.vertices_in[vertex] = []
        self.repository.vertices_number += 1

    def add_an_edge(self,start_vertex:int, end_vertex:int, cost:int):
        self.repository.vertices_out[start_vertex].append(end_vertex)
        self.repository.vertices_in[end_vertex].append(start_vertex)

        cost_elements = ()
        elem = list(cost_elements)
        elem.append(int(start_vertex))
        elem.append(int(end_vertex))
        cost_elements = tuple(elem)

        self.repository.costs[cost_elements] = int(cost)

        self.repository.edges_number += 1




    def find_connected_components(self): # Important
        visited = set()
        components = []

        for vertex in range(self.repository.vertices_number):
            if vertex not in visited:
                component = []
                queue = Queue()
                queue.put(vertex)

                while not queue.empty():
                    current_vertex = queue.get()

                    if current_vertex not in visited:
                        visited.add(current_vertex)
                        component.append(current_vertex)

                        # For undirected graph, we need to consider both outgoing and incoming edges
                        for neighbor in self.repository.vertices_out[current_vertex] + self.repository.vertices_in[current_vertex]:
                            if neighbor not in visited:
                                queue.put(neighbor)

                components.append(component)

        return components

    def dijkstra_shortest_path(self, start_vertex: int, end_vertex: int) -> float: # Important
        # Priority queue to keep track of vertices with their minimum distance from the start vertex
        priority_queue = PriorityQueue()

        # Dictionary to store the shortest distances from start_vertex to other vertices
        shortest_distances = {}
        for vertex in range(self.repository.vertices_number):
            shortest_distances[vertex] = float('inf')

        shortest_distances[start_vertex] = 0.0

        # Put the start vertex in the priority queue
        priority_queue.put((0.0, start_vertex))

        # Dijkstra's algorithm
        while not priority_queue.empty():
            current_distance, current_vertex = priority_queue.get()

            # If we found the end vertex, return its shortest distance
            if current_vertex == end_vertex:
                return shortest_distances[current_vertex]

            # Check the adjacent vertices
            for neighbor in self.repository.vertices_out[current_vertex]:
                # Calculate the new distance
                new_distance = current_distance + self.repository.costs[(current_vertex, neighbor)]

                # If the new distance is shorter than the known shortest distance, update it
                if new_distance < shortest_distances[neighbor]:
                    shortest_distances[neighbor] = new_distance
                    priority_queue.put((new_distance, neighbor))

        # If end_vertex is not reachable from start_vertex, return infinity
        return float('inf')



    def prim_minimum_spanning_tree(self, start_vertex: int):#Important
        # Set to keep track of visited vertices
        visited = set()

        # Priority queue to select the minimum cost edge
        priority_queue = PriorityQueue()

        # Start with the given start_vertex
        visited.add(start_vertex)

        # Add all edges from start_vertex to the priority queue
        for neighbor in self.repository.vertices_out[start_vertex]:
            priority_queue.put((self.repository.costs[(start_vertex, neighbor)], start_vertex, neighbor))

        # List to store the edges in the minimum spanning tree
        minimum_spanning_tree = []

        # Loop until priority queue is empty
        while not priority_queue.empty():
            # Get the minimum cost edge
            cost, u, v = priority_queue.get()

            # If the end vertex of the edge is not visited
            if v not in visited:
                # Add the edge to the minimum spanning tree
                minimum_spanning_tree.append((u, v, cost))

                # Mark the end vertex as visited
                visited.add(v)

                # Add all edges from v to the priority queue
                for neighbor in self.repository.vertices_out[v]:
                    if neighbor not in visited:
                        priority_queue.put((self.repository.costs[(v, neighbor)], v, neighbor))

        return minimum_spanning_tree





    def minimum_spanning_tree(self):
        # Prim's algorithm for finding minimum spanning tree
        visited = [False] * self.repository.vertices_number
        min_heap = [(0, 0)]  # (cost, vertex)
        mst_edges = []

        while min_heap:
            cost, vertex = heapq.heappop(min_heap)
            if not visited[vertex]:
                visited[vertex] = True
                for neighbor in self.repository.vertices_out[vertex]:
                    if not visited[neighbor]:
                        heapq.heappush(min_heap, (self.repository.costs[(vertex, neighbor)], neighbor))
                        mst_edges.append((vertex, neighbor))

        return mst_edges

    def eulerian_circuit(self, mst_edges):
        # Hierholzer's algorithm for finding Eulerian circuit
        graph = {}
        for edge in mst_edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        circuit = []

        def dfs(node):
            while graph[node]:
                neighbor = graph[node].pop()
                graph[neighbor].remove(node)
                dfs(neighbor)
            circuit.append(node)

        dfs(0)

        return circuit[::-1]

    def shortcut(self, circuit):
        # Shortcutting the Eulerian circuit to get Hamiltonian cycle
        visited = [False] * self.repository.vertices_number
        hamiltonian_cycle = []
        for vertex in circuit:
            if not visited[vertex]:
                hamiltonian_cycle.append(vertex)
                visited[vertex] = True
        return hamiltonian_cycle

    def find_hamiltonian_cycle(self):
        # Christofides algorithm to find Hamiltonian cycle
        mst_edges = self.minimum_spanning_tree()
        eulerian_circuit = self.eulerian_circuit(mst_edges)
        hamiltonian_cycle = self.shortcut(eulerian_circuit)
        return hamiltonian_cycle


