import Objects
import RailRoadFile
from RailRoadFile import RailRoad

nodes = []
Gomel = Objects.RailStation("Gomel")
nodes.append(Gomel)
Brest = Objects.RailStation("Brest")
nodes.append(Brest)
Minsk = Objects.RailStation("Minsk")
nodes.append(Minsk)
Grodno = Objects.RailStation("Grodno")
nodes.append(Grodno)
Vitebsk = Objects.RailStation("Vitebsk")
nodes.append(Vitebsk)
Pinsk = Objects.RailStation("Pinsk")
nodes.append(Pinsk)
Polotsk = Objects.RailStation("Polotsk")
nodes.append(Polotsk)
Mogilev = Objects.RailStation("Mogilev")
nodes.append(Mogilev)
Gomel.set_storage(Objects.Goods(Vitebsk, 60))


init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph[Gomel][Gomel] = 50
init_graph[Gomel][Grodno] = 40
init_graph[Brest][Pinsk] = 10
init_graph[Brest][Minsk] = 30
init_graph[Minsk][Polotsk] = 40
init_graph[Minsk][Mogilev] = 40
init_graph[Vitebsk][Pinsk] = 20
init_graph[Vitebsk][Mogilev] = 20

train_1 = Objects.Train(40, Gomel, [Objects.Goods(Vitebsk, '100'), Objects.Goods(Pinsk, '50')])
train_2 = Objects.Train(20, Vitebsk, [Objects.Goods(Minsk, '200'), Objects.Goods(Brest, '80')])
train_3 = Objects.Train(60, Minsk, [Objects.Goods(Grodno, '30'), Objects.Goods(Polotsk, '150')])
rail: RailRoad = RailRoadFile.RailRoad(nodes, init_graph, [train_1, train_2, train_3])
train_1.way_check(rail.graph)
train_2.way_check(rail.graph)
train_3.way_check(rail.graph)