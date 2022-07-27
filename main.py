
from bi_direction_graph import BiDirectionGraph

bi_direct_graph = BiDirectionGraph()
while True:
    fileName = input('What is graph file name: ')
    startNode = input('What is start node?: ')
    goalNode = input('What is goal node?: ')
    print(bi_direct_graph.get_shortest_path(fileName, startNode, goalNode))
    print('')
    is_continued = input('Do you want to continue (y/n) ?: ')
    if (is_continued == 'n'):
        break
