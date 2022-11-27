import matplotlib.pyplot as plt

class Node():
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.radio=None

class MTree():
    def __init__(self,func):
        self.root=None
        self.distance=func

    def rec_add_node(self,padre,node):
        if(padre.children==[]):
            #node.radio = padre.radio - self.distance(padre.data,node.data)
            node.radio = padre.radio/2
            padre.children.append(node)
        else:
            min=padre.radio
            for child in padre.children:
                dist=self.distance(node.data,child.data)
                if( dist < padre.radio):
                    self.rec_add_node(child,node)
                    return
                tmp=dist-padre.radio
                if(tmp < min):
                    min=tmp

            node.radio=min
            #node.radio = padre.radio/2
            padre.children.append(node)
    
    def add(self,padre,node):
        dist=self.distance(padre.data,node.data)
        if( dist < padre.radio):
            if(padre.children==[]):
                node.radio = padre.radio - self.distance(padre.data,node.data)
                #node.radio = padre.radio/2
                padre.children.append(node)
            else:
                for child in node.children:
                    self.add(child,node)
    def add_node(self,data):
        node=Node(data)
        if(self.root==None):
            node.radio=200000
            self.root=node
            return
        else:
            self.rec_add_node(self.root,node)

    def NN(self,padre,hijo,node):
        if(hijo.children==[]):
            return padre.data
        else:
            min=hijo.radio
            nn = hijo.data
            for child in hijo.children:
                tmp = self.NN(hijo,child,node)
                if(tmp < min):
                    min=tmp
                    nn = tmp.data
            return nn
        return padre

    def rec_searchNN(self,padre,hijo,node):
        print("Entre",hijo.data.nombre)
        if(hijo.data==node.data):
            if(hijo.children==[]):
                return padre.data
            else:
                min=hijo.radio
                node_nn= None
                for child in hijo.children:
                    print(child.data.nombre)
                    dist=self.distance(child.data,hijo.data)
                    if( dist < min):
                        min=dist
                        node_nn=child
                return node_nn.data
                

        for child in hijo.children:
            dist=self.distance(hijo.data,node.data)
            if( dist < hijo.radio):
                return self.rec_searchNN(hijo,child,node)
    
    def searchNN(self,data):
        return self.rec_searchNN(None,self.root,Node(data))

    def NNrange(self,node,range):
        for child in node.children:
            self.NNrange(node,range)

    def rec_graph(self,axes,node):
        for child in node.children:
            draw_circle = plt.Circle(child.data.point(), child.radio,fill=False)
            axes.set_aspect(1)
            axes.add_artist(draw_circle)
            self.rec_graph(axes,child)
            plt.plot(child.data.x,child.data.y, marker='.', color="red")

    def graph(self):
        figure, axes = plt.subplots()
        print(axes)
        draw_circle = plt.Circle(self.root.data.point(), self.root.radio,fill=False)
        #axes.set_aspect(1)
        axes.add_artist(draw_circle)
        self.rec_graph(axes,self.root)
        plt.plot(self.root.data.x,self.root.data.y, marker="o", color="red")
        print(axes)
        plt.title('Mtree')
        plt.xlim(-200000,300000)
        plt.ylim(-220000,220000)
        plt.show()
