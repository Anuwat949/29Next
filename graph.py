from typing import Dict
from node import Node
from abc import ABC, abstractmethod


class Graph(ABC):
    """A base class for graphs."""

    def __init__(self, file_name : str = '', start_node_name : str = '', 
                 goal_node_name : str = ''):
        """
        Constructs all the necessary attributes for the graph object.

        Parameters
        ----------
            file_name : str
                name of data file
            start_node_name : str
                name of start node
            goal_node_name : str
                name of goal : node
        """
        self.file_name = file_name
        self.start_node_name = start_node_name
        self.goal_node_name = goal_node_name
        self.graph : Dict[str : Dict[str : Node]] = {}
        
    
    @abstractmethod
    def create_graph(self):
        """Read in data from a given file and construct a graph."""
        pass

    @abstractmethod
    def get_all_neighbor_nodes(self, node_name : str) -> Dict[str , Node]:
        """Retun corresponding all neighbor nodes of a given node name."""
        pass

    def print_graph(self):
        """Print a graph."""
        pass

    def get_shortest_path(self, file_name : str, start_node : str,
                          goal_node : str) -> str:
        """Retun the shortest path in string from start node to goal node."""
        return ''
    
    
