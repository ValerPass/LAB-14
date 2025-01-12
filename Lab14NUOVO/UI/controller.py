import warnings

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._model.buildGrafo()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo è stato creato correttamente"))
        nNodes, nEdges = self._model.getDetails()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {nNodes} nodi e {nEdges} archi"))
        self.pesoMin, self.pesoMax = self._model.getPesiArchi()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha peso minimo {self.pesoMin} e peso massimo {self.pesoMax}"))

        self._view.update_page()

    def handle_countedges(self, e):
        self._view.txt_result2.controls.clear()
        try:
            if float(self._view.txt_name.value) > self.pesoMin and float(self._view.txt_name.value) < self.pesoMax:
                pesoMinoreS = 0
                pesoMaggioreS = 0
                for arco in list(self._model._grafo.edges(data = True)):
                    if arco[2]["weight"] > float(self._view.txt_name.value) :
                        pesoMaggioreS +=1
                    elif arco[2]["weight"] < float(self._view.txt_name.value) :
                        pesoMinoreS +=1
                self._view.txt_result2.controls.append(ft.Text(f"Ci sono {pesoMinoreS} archi con peso < {self._view.txt_name.value} e {pesoMaggioreS} con peso > di {self._view.txt_name.value}"))
            else:
                warnings.warn(f"Attenzione inserire un valore compreso tra {self.pesoMin} e {self.pesoMax} ")
                self._view.txt_result2.controls.append(ft.Text(f"ATTENZIONE, deve inserire un valore compreso tra {self.pesoMin} e {self.pesoMax}"))
                self._view.update_page()
        except ValueError:
            warnings.warn("Attenzione inserire un valore numerico")
            self._view.txt_result2.controls.append(ft.Text(f"ATTENZIONE, deve inserire un valore numerico"))
            self._view.update_page()
        self._view.update_page()
    def handle_search(self, e):
        pass