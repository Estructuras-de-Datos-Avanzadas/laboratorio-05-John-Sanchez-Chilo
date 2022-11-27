from m_tree import *

def distance(nodo1,nodo2):
    return ((nodo1.x-nodo2.x)**2+(nodo1.y-nodo2.y)**2)**(1/2)

mtree= MTree(distance)

class Pais():
    def __init__(self,nombre,x,y):
        self.nombre = nombre
        self.x=x
        self.y=y
    def __eq__(self,other):
        if(self.nombre==other.nombre and self.x==other.x and self.y==other.y):
            return True
        return False
    def __str__(self):
        return self.nombre+" "+str(self.x)+" - "+str(self.y)
    def point(self):
        return (self.x, self.y)

mtree.add_node(Pais("Peru",66477,5983))
mtree.add_node(Pais("Bulgaria",101106,4139))
mtree.add_node(Pais("Bosnia_and_Herzegovina",84584,3870))
mtree.add_node(Pais("Montenegro",250528,3673))
mtree.add_node(Pais("North Macedonia",103485,3639))
mtree.add_node(Pais("Hungary",114600,3586))
mtree.add_node(Pais("Czechia",200245,3080))
mtree.add_node(Pais("Georgia",212561,3030))
mtree.add_node(Pais("Romania",93390,2966))
mtree.add_node(Pais("Gibraltar",215221,2910))
mtree.add_node(Pais("Brazil",102912,2863))
mtree.add_node(Pais("San Marino",175688,2733))
mtree.add_node(Pais("Croatia",149455,2678))
mtree.add_node(Pais("Slovakia",124480,2639))
mtree.add_node(Pais("Argentina",116439,2547))
mtree.add_node(Pais("Armenia",113938,2547))
mtree.add_node(Pais("Lithuania",93390,2525))
mtree.add_node(Pais("Slovenia",202419,2512))
mtree.add_node(Pais("Colombia",98156,2489))
mtree.add_node(Pais("USA",148104,2406))

mtree.graph()

