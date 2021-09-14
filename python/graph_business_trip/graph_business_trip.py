from graph.graph import Graph


def business_trip(graph, citieslist):
    cost = 0
    is_avilable = False
    for i in range(len(citieslist)-1):

        neighbors = graph.get_neighbors(citieslist[i])

        for neighbor in neighbors:
            if neighbor.vertex == citieslist[i+1]:
                cost += neighbor.weight
                is_avilable = True
            else:
                is_avilable = False
        if not is_avilable:
            return f'{is_avilable} , ${0}'

    return f'{is_avilable} , ${cost}'


if __name__ == "__main__":

    graph = Graph()
    Pandora = graph.add_node("Pandora")
    Arendelle = graph.add_node("Arendelle")
    Monstroplolis = graph.add_node("Monstroplolis")
    Narnia = graph.add_node("Narnia")
    Naboo = graph.add_node("Naboo")
    graph.add_edge(Pandora, Arendelle, 70)
    graph.add_edge(Arendelle, Pandora, 130)
    graph.add_edge(Arendelle, Monstroplolis, 99)
    graph.add_edge(Monstroplolis, Narnia, 26)
    graph.add_edge(Monstroplolis, Naboo, 42)
    print(business_trip(graph, [Pandora, Arendelle, Naboo]))
    print(business_trip(graph, [Pandora, Arendelle]))
    print(business_trip(graph, [Monstroplolis, Arendelle, Pandora]))
