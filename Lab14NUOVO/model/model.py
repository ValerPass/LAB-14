import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._Chromosome = DAO.getAllChromosome()
        self._grafo = nx.Graph()

    def getAllChromosome(self):
        return self._Chromosome

    def buildGrafo(self):
        self._grafo.add_nodes_from(self._Chromosome)
        # metodo per aggiungere archi se ho preso il peso di ciascun arco da DAO
        for c in self._grafo.nodes:
            for c1 in self._grafo.nodes:
                if c != c1:
                    edgeW = DAO.getEdgeWeight(c, c1)
                    if len(edgeW) > 0:
                        self._grafo.add_edge(c, c1, weight=edgeW[0])

    def getPesiArchi(self):
        listaArchi = list(self._grafo.edges(data=True))
        listaArchi.sort(key=lambda x: x[2]["weight"])
        return listaArchi[0][2]["weight"], listaArchi[len(listaArchi)-1][2]["weight"]

    def getDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)
