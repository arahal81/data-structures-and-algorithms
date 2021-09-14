from graph_business_trip.graph_business_trip import business_trip
from graph.graph import Graph



def test_cost_for_two_cities():
    graph = Graph()
    Pandora = graph.add_node("Pandora")
    Arendelle = graph.add_node("Arendelle")
    graph.add_edge(Pandora, Arendelle, 80)

    assert business_trip(
        graph, [Pandora, Arendelle]) == 'True , $80'


def test_cost_for_malti_city():
    graph = Graph()
    Pandora = graph.add_node("Pandora")
    Arendelle = graph.add_node("Arendelle")
    Monstroplolis = graph.add_node("Monstroplolis")
    Narnia = graph.add_node("Narnia")
    Naboo = graph.add_node("Naboo")
    graph.add_edge(Pandora, Arendelle, 50)
    graph.add_edge(Arendelle, Pandora, 130)
    graph.add_edge(Arendelle, Monstroplolis, 70)
    graph.add_edge(Monstroplolis, Narnia, 50)
    graph.add_edge(Monstroplolis, Naboo, 30)
    assert business_trip(
        graph, [Pandora, Arendelle, Monstroplolis]) == 'True , $120'


def test_no_dir():
    graph = Graph()
    Pandora = graph.add_node("Pandora")
    Arendelle = graph.add_node("Arendelle")
    Naboo = graph.add_node("Naboo")
    graph.add_edge(Pandora, Arendelle, 80)

    assert business_trip(
        graph, [Pandora, Naboo]) == 'False , $0'


def test_empty_graph():
    graph = Graph()

    assert business_trip(
        graph, []) == 'False , $0'
