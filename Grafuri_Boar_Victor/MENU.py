
class Menu:

    def __init__(self,repository,functions):
        self.repository = repository
        self.functions = functions

    def verify_if_we_have_a_graph(self)->bool:
        if self.repository.vertices_number and self.repository.edges_number:
            return True
        else:
            print("We don't have a graph, please take one from a file or create randomly one")
            return False

    def already_have_graph(self)->bool:
        if self.repository.vertices_number and self.repository.edges_number:
            return True
        else:
            return False

    def show_connected_components(self):
        if self.verify_if_we_have_a_graph():
            components = self.functions.find_connected_components()

            print("Connected Components:")
            for idx, component in enumerate(components, 1):
                print(f"Component {idx}: {component}")



    def ShowMenu(self):
        while True:
            print("\n")
            print("1. Print the number of vertices")
            print("2. Print all vertices")
            print("3. Find an edge between two vertices")
            print("4. Find the in degree and the out degree of a specified vertex")
            print("5. Print all out edges for a specified vertex")
            print("6. Print all in edges for a specified vertex")
            print("7. Print the final points of a vertex")
            print("8. Modify information at a specified vertex")
            print("9. Delete a specified vertex")
            print("10. Delete a specified edge")
            print("11. Copy the entire graph")
            print("12. Write the graph in a file")
            print("13. Read a graph from a file")
            print("14. Create a random graph")
            print("15. Take the copy")
            print("16. Add a vertex")
            print("17. Add an edge")
            print("18. Connected components")
            print("19. Dijkstra shortest path")
            print("20. Prim minimum spanning tree")
            print("21. Hamiltonian_cycle")
            print("0. EXIT\n")

            command = int(input("Input a command -> "))
            print("\n")

            if command == 1 and self.verify_if_we_have_a_graph():
                    print(self.functions.print_the_number_of_vertices())

            elif command == 2 and self.verify_if_we_have_a_graph():
                vertices_list= self.functions.print_all_vertices()

                for index in vertices_list.keys():
                    for vertex in vertices_list[index]:
                        tuple_elements = (index, vertex)
                        keys_cost_list = self.repository.costs.keys()

                        if tuple_elements in keys_cost_list:
                            print(f"{index} -> {vertex} $ {self.repository.costs[tuple_elements]}\n")

            elif command == 3 and self.verify_if_we_have_a_graph():
                start_vertex = int(input("Input first vertex -> "))
                end_vertex = int(input("Input second vertex -> "))
                print("\n")

                if self.functions.find_an_edge_between_two_vertices(start_vertex,end_vertex):
                    print(f"We have an edge between {start_vertex} and {end_vertex}\n")
                else:
                    print(f"We don't have an edge between {start_vertex} and {end_vertex}\n")

            elif command == 4 and self.verify_if_we_have_a_graph():
                vertex = int(input("Input a vertex -> "))
                print("\n")

                if vertex in self.repository.vertices_in.keys():
                    number_degree_in, number_degree_out = self.functions.find_the_in_degree_and_the_out_degree_of_a_specified_vertex(vertex)

                    if number_degree_in or number_degree_out:
                        print(f"We have {number_degree_in} edges witch enter in our vertex and {number_degree_out} edges witch exit form our vertex\n")
                    else:
                        print(f"We don't have edges from or to our vertex\n")
                else:
                    print("We don't have that vertex in our graph")

            elif command == 5 and self.verify_if_we_have_a_graph():
                vertex = int(input("Input a vertex -> "))
                print("\n")

                if vertex in self.repository.vertices_in.keys():

                    vertices_out = self.functions.print_all_out_edges_for_a_specified_vertex(vertex)

                    if vertices_out:
                        for vertex in vertices_out:
                            print(vertex)
                    else:
                        print(f"We don't have edges witch came out from our vertex")
                else:
                    print("We don't have that vertex in our graph")

            elif command == 6 and self.verify_if_we_have_a_graph():
                vertex = int(input("Input a vertex -> "))
                print("\n")

                if vertex in self.repository.vertices_in.keys():

                    vertices_in = self.functions.print_all_in_edges_for_a_specified_vertex(vertex)

                    if vertices_in:
                        for vertex in vertices_in:
                            print(vertex)
                        print("\n")
                    else:
                        print(f"We don't have came in to our vertex\n")
                else:
                    print("We don't have that vertex in our graph")

            elif command == 7 and self.verify_if_we_have_a_graph():
                vertex = int(input("Input a vertex -> "))
                print("\n")

                if vertex in self.repository.vertices_out.keys():
                    vertices_list = self.functions.print_the_final_points_of_a_vertex(vertex)
                    if vertices_list:
                        print(vertices_list)
                    else:
                        print(f"The final point of the vertex {vertex} is himself!\n")
                else:
                    print(f"We don't have that vertex in our graph")

            elif command == 8 and self.verify_if_we_have_a_graph():
                start_vertex = int(input("Input a start_vertex witch you want to modify the costs -> "))
                end_vertex = int(input("Input an end vertex witch you want to modify the costs -> "))
                new_cost = int(input("Input a new costs -> "))
                print("\n")

                if start_vertex in self.repository.vertices_out.keys() and end_vertex in self.repository.vertices_out[start_vertex]:
                    self.functions.modify_the_cost_of_the_edge(start_vertex, end_vertex, new_cost)
                    print("Modify successfully!\n")
                else:
                    print("This edge doesn't exist in our graph!\n")
            elif command == 9 and self.verify_if_we_have_a_graph():
                vertex = int(input("Input a vertex witch you want to delete -> "))
                print("\n")

                if vertex in self.repository.vertices_in.keys():
                    self.functions.delete_a_specified_vertex(vertex)
                    print("Successfully deleted vertex!\n")
                else:
                    print("This vertex doesn't exist in our graph!\n")

            elif command == 10 and self.verify_if_we_have_a_graph():
                start_vertex = int(input("Input a start vertex from an edge witch you want to delete -> "))
                end_vertex = int(input("Input an end vertex from an edge witch you want to delete -> "))
                print("\n")

                if start_vertex in self.repository.vertices_out.keys() and end_vertex in self.repository.vertices_out[start_vertex]:
                    self.functions.delete_a_specified_edge(start_vertex,end_vertex)
                    print("Successfully deleted edge!\n")
                else:
                    print("This edge doesn't exist in our graph!\n")

            elif command == 11 and self.verify_if_we_have_a_graph():
                self.repository.put_a_graph_in_a_copy()
                print("Successfully copied!\n")
            elif command == 12 and self.verify_if_we_have_a_graph():
                self.repository.put_a_graph_in_a_file()
                print("Successfully add the graph in the file!")
            elif command == 13 and not self.already_have_graph() :
                self.repository.get_a_graph_from_file()

                if self.repository.vertices_number or self.repository.edges_number:
                    print("Successfully read a graph!\n")
                else:
                    print("Unsuccessful reading graph!\n")

            elif command == 14 and not self.already_have_graph():
                vertices_number = int(input("Input the number of vertices -> "))
                edges_number = int(input("Input the number of edges ->"))

                if vertices_number * vertices_number >= edges_number:
                    self.functions.random_graph(vertices_number,edges_number)
                else:
                    print("Error!\n")

            elif command == 15 and self.verify_if_we_have_a_graph():
                self.repository.get_the_copied_graph()

            elif command == 16 and self.verify_if_we_have_a_graph():
                vertex = int(input("Input a vertex -> "))

                if vertex in self.repository.vertices_out.keys():
                    print("Vertices already exist\n")
                else:
                    self.functions.add_a_vertex(vertex)
                    print("Successfully added")

            elif command == 17 and self.verify_if_we_have_a_graph():
                start_vertex = int(input("Input a start vertex -> "))
                end_vertex = int(input("Input an end vertex -> "))
                cost = int(input("Input a cost -> "))

                if start_vertex in self.repository.vertices_out.keys() and end_vertex in self.repository.vertices_out.keys():
                    print("Invalid vertices\n")
                else:
                    self.functions.add_an_edge(start_vertex, end_vertex, cost)
                    print("Successfully added")

            elif command == 18 and self.verify_if_we_have_a_graph():
                if not self.show_connected_components():
                    print("No connected components")

            elif command == 19 and self.verify_if_we_have_a_graph():
                start_vertex = int(input("Input the start vertex -> "))
                end_vertex = int(input("Input the end vertex -> "))

                if start_vertex in self.repository.vertices_out.keys() and end_vertex in self.repository.vertices_out.keys():
                    shortest_distance = self.functions.dijkstra_shortest_path(start_vertex, end_vertex)
                    if shortest_distance != float('inf'):
                        print(f"The lowest cost walk from {start_vertex} to {end_vertex} is {shortest_distance}\n")
                    else:
                        print(f"No path exists from {start_vertex} to {end_vertex}\n")
                else:
                    print("Invalid vertices!\n")

            elif command == 20 and self.verify_if_we_have_a_graph():
                start_vertex = int(input("Input the start vertex -> "))
                if start_vertex in self.repository.vertices_out.keys():
                    minimum_spanning_tree = self.functions.prim_minimum_spanning_tree(start_vertex)
                    if minimum_spanning_tree:
                        print("Minimum Spanning Tree:")
                        total_cost = 0
                        for edge in minimum_spanning_tree:
                            print(f"{edge[0]} - {edge[1]} : {edge[2]}")
                            total_cost += edge[2]
                        print("Total cost:", total_cost)
                    else:
                        print("The graph might not be connected!")
                else:
                    print("Invalid vertex!")


            elif command == 21 and self.verify_if_we_have_a_graph():
                hamiltonian_cycle = self.functions.find_hamiltonian_cycle()

                if hamiltonian_cycle:
                    print("Hamiltonian cycle:")
                    for vertex in hamiltonian_cycle:
                        print(vertex)
                else:
                    print("No Hamiltonian cycle exists!")


            elif command == 0:
                print("You exit form the program!\n")
                break
            elif command < 0 or command > 21:
                print("Invalid command!\n")