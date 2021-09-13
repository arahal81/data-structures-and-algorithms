from graph.graph import Graph


def business_trip(graph, cityislist):
    cost = 0
    avilable = False
    for i in range(len(cityislist)-1):

        neighbors = graph.get_neighbors(cityislist[i])

        for neighbor in neighbors:
            if neighbor.vertex.value == cityislist[i+1]:
                cost += neighbor.weight
                avilable = True

    return f'{avilable} , ${cost}'
