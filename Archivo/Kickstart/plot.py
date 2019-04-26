# Plot interactivo sobre los algoritmos y sus puntuaciones en Kickstart

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from pyexcel_ods import get_data

freqs = np.arange(2, 20, 3)
prob_size = [3,3,3,3,3,3,3,3,3,3,3,4,3,3,4,3]
active_alg = []
for i in range(24):
    active_alg.append(1)
datos = get_data("plot.ods")
datos = datos["Sheet1"]
nombres = datos[0]
datos = datos[1:len(datos)]
nombres_rondas = ["Pr19", "A19", "B19", "A18","B18","C18","D18","E18","F18","G18","H18","C17","D17","E17","F17","G17"]
def gettingHeights(datos, prob_size, active_alg):
    v = []
    for i in range(len(prob_size)):
        v.append(0)

    it = 0
    for i in range(len(prob_size)):
        s = 0
        for j in range(prob_size[i]):
            mx = 0
            for z in range(len(datos[it])):
                if(datos[it][z] > mx and active_alg[z] == 1):
                    mx = datos[it][z]


            s = s + mx
            it += 1
        v[i] = s
    return v



fig, ax = plt.subplots()
heights = gettingHeights(datos, prob_size, active_alg)
y_pos = np.arange(len(nombres_rondas))
plt.subplots_adjust(bottom=0.5)
heights = np.asarray(heights)
l = plt.bar(y_pos, heights, align='center', alpha=0.5)
for i in range(len(l)):
    l[i].set_height(0)
    heights[i] = 0
for i in range(len(active_alg)):
    active_alg[i] = 0
plt.xticks(y_pos, nombres_rondas)
av = np.average(heights)
plt.title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))


class Index:
    v = []
    p = []
    d = []

    def set(self, active_alg, prob_size, datos):
        self.v = active_alg
        self.p = prob_size
        self.d = datos


    def FuerzaBruta(self, event):
        i = 0
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def ProgramacionDin(self, event):
        i = 1
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def Simplif(self, event):
        i = 2
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def Greedy(self, event):
        i = 3
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def SumaP(self, event):
        i = 4
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def BFS(self, event):
        i = 5
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def BFSFuente(self, event):
        i = 6
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def BB(self, event):
        i = 7
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def DFS(self, event):
        i = 8
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def Kruskal(self, event):
        i = 9
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def Recurs(self, event):
        i = 10
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def Dijkstra(self, event):
        i = 11
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def Preproc(self, event):
        i = 12
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def BitMasks(self, event):
        i = 13
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def OptDec(self, event):
        i = 14
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def Cont(self, event):
        i = 15
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def ArbolSegm(self, event):
        i = 16
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def ArbolSegmMod(self, event):
        i = 17
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def ExpRap(self, event):
        i = 18
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def Floyd(self, event):
        i = 19
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def Bubble(self, event):
        i = 20
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def Memoizacion(self, event):
        i = 21
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def SweepLine(self, event):
        i = 22
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()

    def Constructivo(self, event):
        i = 23
        self.v[i] = 1-self.v[i]
        heights = gettingHeights(self.d, self.p, self.v)

        for j in range(len(l)):
            l[j].set_height(heights[j])
        if(self.v[i] == 1):
            b[i].color = 'lightgrey'
        else:
            b[i].color = 'dimgray'
        b[i].hovercolor = b[i].color
        b[i].ax.set_facecolor(b[i].color)
        av = np.average(heights)
        ax.set_title("Gráfica con puntuaciones personalizadas, con una media de " + "{:.2f}".format(av,2))

        plt.draw()



callback = Index()
callback.set(active_alg, prob_size, datos)
button_pos = []
button_pos.append(plt.axes([0.01, 0.05, 0.22, 0.05]))
button_pos.append(plt.axes([0.24, 0.05, 0.22, 0.05]))
button_pos.append(plt.axes([0.47, 0.05, 0.22, 0.05]))
button_pos.append(plt.axes([0.70, 0.05, 0.22, 0.05]))

button_pos.append(plt.axes([0.01, 0.12, 0.22, 0.05]))
button_pos.append(plt.axes([0.24, 0.12, 0.22, 0.05]))
button_pos.append(plt.axes([0.47, 0.12, 0.22, 0.05]))
button_pos.append(plt.axes([0.70, 0.12, 0.22, 0.05]))

button_pos.append(plt.axes([0.01, 0.19, 0.22, 0.05]))
button_pos.append(plt.axes([0.24, 0.19, 0.22, 0.05]))
button_pos.append(plt.axes([0.47, 0.19, 0.22, 0.05]))
button_pos.append(plt.axes([0.70, 0.19, 0.22, 0.05]))

button_pos.append(plt.axes([0.01, 0.26, 0.22, 0.05]))
button_pos.append(plt.axes([0.24, 0.26, 0.22, 0.05]))
button_pos.append(plt.axes([0.47, 0.26, 0.22, 0.05]))
button_pos.append(plt.axes([0.70, 0.26, 0.22, 0.05]))

button_pos.append(plt.axes([0.01, 0.33, 0.22, 0.05]))
button_pos.append(plt.axes([0.24, 0.33, 0.22, 0.05]))
button_pos.append(plt.axes([0.47, 0.33, 0.22, 0.05]))
button_pos.append(plt.axes([0.70, 0.33, 0.22, 0.05]))

button_pos.append(plt.axes([0.01, 0.40, 0.22, 0.05]))
button_pos.append(plt.axes([0.24, 0.40, 0.22, 0.05]))
button_pos.append(plt.axes([0.47, 0.40, 0.22, 0.05]))
button_pos.append(plt.axes([0.70, 0.40, 0.22, 0.05]))
b = []
b.append(Button(button_pos[len(b)], 'Fuerza Bruta', color="dimgray"))
b[len(b)-1].on_clicked(callback.FuerzaBruta)
b.append(Button(button_pos[len(b)], 'Progr. Dinámica', color="dimgray"))
b[len(b)-1].on_clicked(callback.ProgramacionDin)
b.append(Button(button_pos[len(b)], 'Simplif. del prob.', color="dimgray"))
b[len(b)-1].on_clicked(callback.Simplif)
b.append(Button(button_pos[len(b)], 'Greedy', color="dimgray"))
b[len(b)-1].on_clicked(callback.Greedy)
b.append(Button(button_pos[len(b)], 'Suma Prefija', color="dimgray"))
b[len(b)-1].on_clicked(callback.SumaP)
b.append(Button(button_pos[len(b)], 'BFS', color="dimgray"))
b[len(b)-1].on_clicked(callback.BFS)
b.append(Button(button_pos[len(b)], 'BFS fuentes mult.', color="dimgray"))
b[len(b)-1].on_clicked(callback.BFSFuente)
b.append(Button(button_pos[len(b)], 'Búsqueda binaria', color="dimgray"))
b[len(b)-1].on_clicked(callback.BB)
b.append(Button(button_pos[len(b)], 'DFS', color="dimgray"))
b[len(b)-1].on_clicked(callback.DFS)
b.append(Button(button_pos[len(b)], 'Kruskal', color="dimgray"))
b[len(b)-1].on_clicked(callback.Kruskal)
b.append(Button(button_pos[len(b)], 'Recursividad', color="dimgray"))
b[len(b)-1].on_clicked(callback.Recurs)
b.append(Button(button_pos[len(b)], 'Dijkstra', color="dimgray"))
b[len(b)-1].on_clicked(callback.Dijkstra)
b.append(Button(button_pos[len(b)], 'Preprocesamiento', color="dimgray"))
b[len(b)-1].on_clicked(callback.Preproc)
b.append(Button(button_pos[len(b)], 'Máscaras de bits', color="dimgray"))
b[len(b)-1].on_clicked(callback.BitMasks)
b.append(Button(button_pos[len(b)], 'Optimiz.->Decisión', color="dimgray"))
b[len(b)-1].on_clicked(callback.OptDec)
b.append(Button(button_pos[len(b)], 'Contar en binario', color="dimgray"))
b[len(b)-1].on_clicked(callback.Cont)
b.append(Button(button_pos[len(b)], 'Árbol de segmento', color="dimgray"))
b[len(b)-1].on_clicked(callback.ArbolSegm)
b.append(Button(button_pos[len(b)], 'Árbol segm. mod.', color="dimgray"))
b[len(b)-1].on_clicked(callback.ArbolSegmMod)
b.append(Button(button_pos[len(b)], 'Exponenc. rápida', color="dimgray"))
b[len(b)-1].on_clicked(callback.ExpRap)
b.append(Button(button_pos[len(b)], 'Floyd-Warshall', color="dimgray"))
b[len(b)-1].on_clicked(callback.Floyd)
b.append(Button(button_pos[len(b)], 'Bubble Sort', color="dimgray"))
b[len(b)-1].on_clicked(callback.Bubble)
b.append(Button(button_pos[len(b)], 'Memoizacion', color="dimgray"))
b[len(b)-1].on_clicked(callback.Memoizacion)
b.append(Button(button_pos[len(b)], 'Sweep line', color="dimgray"))
b[len(b)-1].on_clicked(callback.SweepLine)
b.append(Button(button_pos[len(b)], 'Constructivo', color="dimgray"))
b[len(b)-1].on_clicked(callback.Constructivo)



plt.show()
