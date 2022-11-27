from mtree import *
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

def distance(pais1,pais2):
    return ((pais1.x-pais2.x)**2+(pais1.y-pais2.y)**2)**(1/2)

tree = MTree(distance, max_node_size=20)


tree.add(Pais("Peru",66477,5983))
tree.add(Pais("Bulgaria",101106,4139))
tree.add(Pais("Bosnia_and_Herzegovina",84584,3870))
tree.add(Pais("Montenegro",250528,3673))
tree.add(Pais("North Macedonia",103485,3639))
tree.add(Pais("Hungary",114600,3586))
tree.add(Pais("Czechia",200245,3080))
tree.add(Pais("Georgia",212561,3030))
tree.add(Pais("Romania",93390,2966))
tree.add(Pais("Gibraltar",215221,2910))
tree.add(Pais("Brazil",102912,2863))
tree.add(Pais("San Marino",175688,2733))
tree.add(Pais("Croatia",149455,2678))
tree.add(Pais("Slovakia",124480,2639))
tree.add(Pais("Argentina",116439,2547))
tree.add(Pais("Armenia",113938,2547))
tree.add(Pais("Lithuania",93390,2525))
tree.add(Pais("Slovenia",202419,2512))
tree.add(Pais("Colombia",98156,2489))
tree.add(Pais("USA",148104,2406))

rpta=tree.search(Pais("Hungary",114600,3586),2)
for r in rpta:
    print(r.nombre)