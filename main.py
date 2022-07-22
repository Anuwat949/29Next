# import sys
import app
# fileName = sys.argv[1]
# startNode = sys.argv[2]
# goalNode = sys.argv[3]

fileName=input('What is graph file name: ')
startNode=input('What is start node?: ')
goalNode=input('What is goal node?: ')
print(app.get_shortest_route(fileName,startNode,goalNode))