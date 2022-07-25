"""
Find the shortest route from start node to goal Node
param 1: name of example file in csv
param 2: name of start node
param 3: name of goal node
return : string => the shortest route
"""
def get_shortest_route(fileName,startNode,goalNode):
    # Use an adjacency list design pattern to represents a graph
    # After that use Dijkstra's algorithm to find the shortest paths between nodes in a graph
    # Note: Can use only built-in data structures => Lists, Dictionary, Tuple and Set

    graphRep={} # graph representation (adjacency list design pattern)

    # read file and construct graph
    # exp: {
    #       'D': {'A': {'distance': 3}, 'G': {'distance': 6}}, 
    #       'E': {'A': {'distance': 4}, 'F': {'distance': 6}},
    #       ...
    #       }
    with open(fileName,'r') as f:
        for line in f:
            line_strip=line.strip()
            nodeRelationship=line_strip.split(',')
            # create a list of neighbor nodes(contains node name and distance) of a given node
            if nodeRelationship[2]!='0':
                if not nodeRelationship[0] in graphRep:
                    graphRep[nodeRelationship[0]]={}
                if not nodeRelationship[1] in graphRep:
                    graphRep[nodeRelationship[1]]={}
                graphRep[nodeRelationship[0]][nodeRelationship[1]]={'distance':int(nodeRelationship[2])}
                graphRep[nodeRelationship[1]][nodeRelationship[0]]={'distance':int(nodeRelationship[2])}
            else:
                if not nodeRelationship[0] in graphRep:
                    graphRep[nodeRelationship[0]]={}


    # To find shortest path
    # 1. create two empty dictionaries: visited and unvisited dict 
    # 2. for now, we have not visisted any node yet. so we assume that the distance is very very far away as much as possible -> let's say infinity, and its previous node is none
    #       exp. {'A': {'preNode': None, 'distance': inf}, 'B': {'preNode': None, 'distance': inf},..}
    # 3. select start node and initialize its status => since we know that going from start node to itself means that we are not going anywhere, so distance is 0, and its previous node is none
    # 4. start from the given start node, find all its neighbor nodes available in unvisted node dict, then calculate the distance between the given start node and each neighbor node
    # 5. every neighbor nodes of the start node, compare the new calculated distance with its previous distance; 
    #       if the calculated distances is shorter than the previous one, we assign new shorter distance and new previous node  
    # 6. after that we move start node to visisted list
    # 7. find the next start node by looking through unvisted node dict and then select the node with the shortest distance, 
    #       then assign it as the start node
    # 8. repeat No. 4 again until there is no more unvisted node left

    visistedNodeDict={}
    unvistedNodeDict={}
    # initialize unvisited node list
    for key in graphRep.keys():
        unvistedNodeDict[key]={'preNode':None,'distance':float('inf')}

    # check for invalid input node
    if not startNode in graphRep:
        return "Undefine Start Node: "+startNode
    if not goalNode in graphRep:
        return "Undefine Goal Node: "+goalNode


    # set start node: 0 distance, previous node is None
    curStartNodeName=startNode
    curStartNode=unvistedNodeDict[startNode]
    curStartNode['distance']=0

    # start finding shortest path
    while len(unvistedNodeDict)>0:
        for neighborNodeKey in graphRep[curStartNodeName].keys():

            # calculate distance from the current start node to its neighbor node
            # ignore already visisted node, if shorter path is found then update this value to distance, and update new previous node
            
            if neighborNodeKey in visistedNodeDict:
                continue
            tempDistance=curStartNode['distance']+graphRep[curStartNodeName][neighborNodeKey]['distance']
            if tempDistance < unvistedNodeDict[neighborNodeKey]['distance'] :
                unvistedNodeDict[neighborNodeKey]['distance']=tempDistance
                unvistedNodeDict[neighborNodeKey]['preNode']=curStartNodeName


        # move curStartNode from unvisited node dict to visisted node dict
        visistedNodeDict[curStartNodeName]=unvistedNodeDict[curStartNodeName]
        unvistedNodeDict.pop(curStartNodeName)

        #get next node to examine by findind the unvisted node that has the shortest distance
        nextStartNode={}
        for leftUnvistedNodeKey in unvistedNodeDict.keys():
            if len(nextStartNode)==0:
                nextStartNode=unvistedNodeDict[leftUnvistedNodeKey]
                curStartNodeName=leftUnvistedNodeKey
            else:
                if nextStartNode['distance'] > unvistedNodeDict[leftUnvistedNodeKey]['distance']:
                    nextStartNode=unvistedNodeDict[leftUnvistedNodeKey]
                    curStartNodeName=leftUnvistedNodeKey
                    

        
        # set current start node for the next loop
        curStartNode=nextStartNode
 
        
    # constructing answer in string format 
    curNode=goalNode
    path=''
    while True:
        if curNode in visistedNodeDict:
            if curNode==goalNode:
                path=curNode
            else:
                path=curNode+"->"+path
            preNode=visistedNodeDict[curNode]['preNode']
            
            if preNode==None and curNode==startNode :
                path='Path from '+startNode+' to '+goalNode+' is '+path+', and have cost '+str(visistedNodeDict[goalNode]['distance'])+'.'
                break
            if preNode==None and curNode!=startNode:
                path='Path from '+startNode+' to '+goalNode+' is not found'
                break
            curNode=preNode
    
    return path

