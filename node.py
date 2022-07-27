
from typing import Union


class Node:
    """A class to representation of each node in graph."""

    def __init__(self, node_name : str, prev_node_name : Union[str,None], 
                 distance : Union[int,float]):
        """
        Constructs all the necessary attributes for the node object.

        Parameters
        ----------
            node_name : str
                node name
            prev_node : str
                previous node name
            distance : int, float
                distance from previous node
        """
        self.__node_name = node_name
        self.__prev_node_name = prev_node_name
        self.__distance = distance

    @property
    def node_name(self):
        """Get or set node name."""
        return self.__node_name

    @node_name.setter
    def node_name(self, node_name):
        self.__node_name = node_name

    @property
    def previous_node_name(self):
        """Get or set previous node name."""
        return self.__prev_node_name
    
    @previous_node_name.setter
    def previous_node_name(self, prev_node_name):
        self.__prev_node_name = prev_node_name

    @property
    def distance(self):
        """Get or set distance from previous node."""
        return self.__distance
    
    @distance.setter
    def distance(self, distance):
        self.__distance = distance

    def __str__(self):
        return f"{{ node name: { self.node_name }, \
                    previous node: { self.previous_node_name }, \
                    distance:  { self.distance } }}"

    def __repr__(self):
        return f"{{ node name: { self.node_name }, \
                    previous node: { self.previous_node_name }, \
                    distance:  { self.distance } }}"


        

