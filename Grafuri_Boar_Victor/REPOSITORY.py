
class Repository:
    def __init__(self,file_name:str):
        self.vertices_in = {}
        self.vertices_out = {}
        self.costs = {}
        self.vertices_number = 0
        self.edges_number = 0
        self.file_name = file_name

    def get_a_graph_from_file(self):
        self.vertices_in.clear()
        self.vertices_out.clear()
        self.costs.clear()
        self.vertices_number = 0
        self.edges_number = 0

        with open(self.file_name, "r") as file:
            information = file.read()

            if information:
                information = information.split("\n")

                size = information[0]

                size = size.split(" ")

                self.vertices_number = int(size[0])
                self.edges_number = int(size[1])

                for index in range(0,self.vertices_number):
                    self.vertices_in[index] = []
                    self.vertices_out[index] = []

                for index in range(1,self.edges_number + 1):
                    start_vertex, end_vertex, cost = information[index].split(" ")
                    self.vertices_out[int(start_vertex)].append(int(end_vertex))
                    self.vertices_in[int(end_vertex)].append(int(start_vertex))

                    cost_elements = ()
                    elem = list(cost_elements)
                    elem.append(int(start_vertex))
                    elem.append(int(end_vertex))
                    cost_elements = tuple(elem)

                    self.costs[cost_elements] = int(cost)

    def put_a_graph_in_a_file(self):
        with open(self.file_name, "w") as file:

            file.write(f"{self.vertices_number} {self.edges_number}\n")

            for index in range(0,self.vertices_number):
                for vertex in self.vertices_out[index]:
                    tuple_elements = (index, vertex)
                    keys_cost_list = self.costs.keys()

                    if tuple_elements in keys_cost_list:
                        file.write(f"{index} {vertex} {self.costs[tuple_elements]}\n")


    def put_a_graph_in_a_copy(self):
        with open("copy_graph.txt", "w") as file:

            file.write(f"{self.vertices_number} {self.edges_number}\n")

            for index in range(0,self.vertices_number):
                for vertex in self.vertices_out[index]:
                    tuple_elements = (index, vertex)
                    keys_cost_list = self.costs.keys()

                    if tuple_elements in keys_cost_list:
                        file.write(f"{index} {vertex} {self.costs[tuple_elements]}\n")


    def get_the_copied_graph(self):
        self.vertices_in.clear()
        self.vertices_out.clear()
        self.costs.clear()
        self.vertices_number = 0
        self.edges_number = 0

        with open("copy_graph.txt", "r") as file:
            information = file.read()

            if information:
                information = information.split("\n")

                size = information[0]

                size = size.split(" ")

                self.vertices_number = int(size[0])
                self.edges_number = int(size[1])

                for index in range(0, self.vertices_number):
                    self.vertices_in[index] = []
                    self.vertices_out[index] = []

                for index in range(1, self.edges_number + 1):
                    start_vertex, end_vertex, cost = information[index].split(" ")
                    self.vertices_out[int(start_vertex)].append(int(end_vertex))
                    self.vertices_in[int(end_vertex)].append(int(start_vertex))

                    cost_elements = ()
                    elem = list(cost_elements)
                    elem.append(int(start_vertex))
                    elem.append(int(end_vertex))
                    cost_elements = tuple(elem)

                    self.costs[cost_elements] = int(cost)