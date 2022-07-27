from typing import Dict
from graph import Graph
from node import Node


class BiDirectionGraph(Graph):
    """A class to represent a bi-direction graph."""

    def __init__(self):
        """
        Constructs all the necessary attributes for the BiDirectinGraph 
        object.
        """
        Graph.__init__(self, '', '', '')
        self.__unvisited_node_dict : Dict[str, Node] = {}
        self.__visited_node_dict : Dict[str, Node] = {}

    def __initialize_unvisited_node(self):
        """
        Generate and initialize unvisited nodes in the graph to 
        unvisited node dictionary.
        """
        self.__clear_unvisited_node_dict()
        for node_name in self.graph.keys():
            self.__unvisited_node_dict[node_name] \
                = Node(node_name, None, float('inf'))

    def __clear_unvisited_node_dict(self):
        """Empty unvisited node dictionary."""
        self.__unvisited_node_dict.clear()

    def __clear_visited_node_dict(self):
        """Empty visited node dictionary"""
        self.__visited_node_dict.clear()

    def __get_shorted_dist_unvisited_node(self) -> Node:
        """
        Return a single node (Node) in unvisited node dictionary that has
        the shortest distance.
        """
        shortest_dist_node : Node = None
        for node_name in self.__unvisited_node_dict:
            if shortest_dist_node == None:
                shortest_dist_node = self.__unvisited_node_dict[node_name]
            else:
                if (shortest_dist_node.distance > 
                        self.__unvisited_node_dict[node_name].distance):
                    shortest_dist_node = self.__unvisited_node_dict[node_name]
        return shortest_dist_node

    def __is_node_visited(self, node_name : str) -> bool:
        """
        Check if the given node name has been visited yet

        Parameters:
            node_name (str) : node name to check
        Return:
            True (boolean) : node has been visited
            False (boolean) : node has not been visited
        """
        if node_name in self.__visited_node_dict:
            return True
        else : 
            return False

    def __update_node(self, node : Node, distance : int, prev_node: Node) -> bool:
        """
        Update a given node's attributes: distance and previous node

        Parameters:
            node (Node) : Node to update
            distance (int) : new distance value to update
            prev_node (Node) : new previous node to update

        Return:
            True (boolean) : if successfully updated
            False (boolean) : if failed update
        """
        node.distance=distance
        node.previous_node_name=prev_node.node_name
        return True

    def __update_node_to_visited_stat(self, node_name : str) -> bool:
        """
        Move the given node from unvisited node dictionary to visited 
        node dictionary

        Parameters:
            node_name (str) : node name to move

        Return:
            True (boolean) : if successfully moved
            False (boolean) : if failed to move
        """
        if node_name not in self.__unvisited_node_dict:
            return False
        else : 
            self.__visited_node_dict[node_name] \
                = self.__unvisited_node_dict[node_name]
            self.__unvisited_node_dict.pop(node_name)
            return True

    def __get_full_path(self, start_node_name : str, goal_node_name : str) -> str:
        """
        Return path taking from start node to goal node

        Parameters:
            start_node_name (str) : name of start node 
            goal_node_name (str) : name of goal node

        Return:
            path (str) : full path and cost that it takes from start node to 
                goal node exp. 'Path from A to B is A->B, and have cost 5.'
        """
        cur_node_name = goal_node_name
        path=''
        while True:
            if cur_node_name == goal_node_name:
                path = cur_node_name
            else:
                path = cur_node_name + "->" + path
            prev_node_name = self.__visited_node_dict[cur_node_name].previous_node_name
            if (prev_node_name == None) and (cur_node_name == start_node_name):
                path = 'Path from ' + start_node_name + ' to ' \
                        + goal_node_name + ' is ' + path \
                        + ', and have cost ' \
                        + str(self.__visited_node_dict[goal_node_name].distance) + '.'
                break
            if (prev_node_name == None) and (cur_node_name != start_node_name):
                path = 'Path from ' + start_node_name + ' to ' \
                        + goal_node_name + ' is not found.'
                break
            cur_node_name = prev_node_name
        return path

    def calc_distance(self, start_node : Node, neighbor_node : Node) -> int:
        """
        Return calculated distance between two given node

        Parameters: 
            start_node (Node) : start node
            neighbor_node (Node) : neighbor node

        Return:
            distance (int) : the calculated distance between two nodes
        """
        # check if start and neighbor node are eligible for calculating distance
        if isinstance(start_node, Node) and isinstance(neighbor_node, Node):
            if start_node.node_name == neighbor_node.previous_node_name:
                if (isinstance(start_node.distance, (int, float, complex)) and not 
                    isinstance(start_node.distance, bool) and 
                    isinstance(neighbor_node.distance, (int, float, complex)) and not 
                    isinstance(neighbor_node.distance, bool)):
                    if (start_node.distance < 0) or (neighbor_node.distance < 0):
                        raise ValueError('indicated distance(s) is less than 0')
                    return start_node.distance + neighbor_node.distance
                else:
                    raise ValueError('indicated distance(s) is not a number')
            else: 
                raise ValueError('start_node and neighbor_node are not connected')
        else:
            raise ValueError('start_node or neighbor_node is not an instance of Node')

    def create_graph(self, file_name) -> bool:
        """
        Create a graph corresponding to read in data

        Parameters:
            file_name (str) : file name of a given graph's data

        Return:
            True (boolean) : if a graph was created successfully
        """
        try:
            self.graph.clear()
            with open(file_name, 'r') as file:
                # read file line by line
                for line in file:
                    read_in_data=line.strip().split(',')
                    if read_in_data[2] != '0':
                        first_node = Node(read_in_data[0], read_in_data[1], int(read_in_data[2]))
                        second_node = Node(read_in_data[1], read_in_data[0], int(read_in_data[2]))
                        # check if read in nodes already exist in the graph
                        # if not, add new node to the graph
                        if first_node.node_name not in self.graph:
                            self.graph[first_node.node_name] = {}
                        if second_node.node_name not in self.graph:
                            self.graph[second_node.node_name] = {}
                        # add nodes(neighbor nodes) to the graph to its corresponding nodes
                        self.graph[first_node.node_name][second_node.node_name] = second_node
                        self.graph[second_node.node_name][first_node.node_name] = first_node
                    else:
                        first_node = Node(read_in_data[0], None, 0)
                        # check if read in nodes already exist in the graph
                        # if not, add new node to the graph
                        # since distance is 0 , so no adding neighbor node
                        if first_node.node_name not in self.graph:
                            self.graph[first_node.node_name] = {}
            return True
        except OSError:
            raise OSError('no such file or directory')
        except ValueError:
            raise ValueError('could not convert data into a graph')
        except IndexError:
            raise IndexError('list index out of range')
        
    def get_all_neighbor_nodes(self, node_name : str) -> Dict[str, Node]:
        """
        Return all neighbor nodes of the given node node
        
        Parameters: 
            node_name (str) : name of node
        
        Return:
            nodes (Dict[str, Node]) : all neighbor nodes of the 
                given node name
        """
        try:
            return self.graph[node_name]
        except KeyError:
            raise KeyError('node: ' + node_name + ' doe not exist')

    def get_shortest_path(self, file_name : str, start_node : str, goal_node : str) -> str:
        """
        Calculate the shortest path between start node and goal node 
        and return that shortest path

        Parameters:
            file_name (str) : file name of graph data
            start_node (str) : name of start node 
            goal_node (str) : name of goal node
        
        Return:
            path (str) : full path and cost that it takes from start node to 
                goal node exp. 'Path from A to B is A->B, and have cost 5.'
        """
        self.file_name = file_name
        self.start_node_name = start_node
        self.goal_node_name = goal_node
        self.create_graph(file_name)

        # if start and goal node do exist, then return path not found
        if self.start_node_name not in self.graph:
            return 'a given start node: ' + self.start_node_name + ' does not exist'
        if self.goal_node_name not in self.graph:
            return 'a given goal node: ' + self.goal_node_name + ' does not exist'

        # clear all previous data : graph, visited and unvisited node dictionary
        self.__clear_visited_node_dict()
        self.__initialize_unvisited_node()
        self.__unvisited_node_dict[self.start_node_name].distance = 0

        # Dijkstra's algorithm
        while len(self.__unvisited_node_dict) > 0:
            cur_node = self.__get_shorted_dist_unvisited_node()
            for neighbor_node in self.get_all_neighbor_nodes(cur_node.node_name).values():
                if self.__is_node_visited(neighbor_node.node_name) :
                    continue
                new_calc_distance = self.calc_distance(cur_node,neighbor_node)
                if (new_calc_distance < self.__unvisited_node_dict[neighbor_node.node_name].distance):
                    self.__update_node(self.__unvisited_node_dict[neighbor_node.node_name], 
                                       new_calc_distance, cur_node)
            self.__update_node_to_visited_stat(cur_node.node_name)
        return self.__get_full_path(self.start_node_name, self.goal_node_name)

    def print_graph(self):
        """
        Pretty print a given graph
        """
        print('{')
        for node_name in self.graph:
            print(' ' + str(node_name) + ' : { ', end = '')
            for neighbor_name in self.graph[node_name]:
                print( str(self.graph[node_name][neighbor_name]) + ', ', end = '' )
            print(' },')        
        print('}')

            
            




    


    
    