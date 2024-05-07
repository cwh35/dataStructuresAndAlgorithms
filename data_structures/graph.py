# Data Structure - Graph

# undirected graph - no direction between 2 nodes
# individual entities are called nodes
# nodes are connected by edges

# example: Facebook Friend suggestion
# example: flight routes (directed graph)

# in a tree, there should only be 1 path between 2 nodes
# edges can be weighted in a graph (weighted graph) 
## ex: distance between 2 cities
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graphDict = {}
        for start, end in self.edges: # start and end are for unpacking tuples, key = starting point
            if start in self.graphDict: # if key already exists
                self.graphDict[start].append(end)
            else:
                self.graphDict[start] = [end]
        print(self.graphDict)

    def getPaths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self.graphDict:
            return []
        
        paths = []
        for node in self.graphDict[start]:
            if node not in path:
                newPaths = self.getPaths(node, end, path)
                for p in newPaths:
                    paths.append(p)

        return paths
    
    def getShortestPath(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path
        
        if start not in self.graphDict:
            return None
        
        shortestPath = None
        for node in self.graphDict[start]:
            if node not in path:
                sp = self.getShortestPath(node, end, path)
                if sp:
                    if shortestPath is None or len(sp) < len(shortestPath):
                        shortestPath = sp

        return shortestPath

if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    route_graph = Graph(routes)

    start = "Paris"
    end = "New York"
    print(route_graph.getShortestPath(start, end))