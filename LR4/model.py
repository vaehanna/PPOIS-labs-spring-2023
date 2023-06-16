from States import *
from Add import *
from Del import *


class MainWindow(QMainWindow):

    def init_button(self, label, size_x, size_y, move_x, move_y, fun):
        button = QPushButton(label, self)
        button.resize(size_x, size_y)
        button.move(move_x, move_y)
        button.clicked.connect(fun)
        return button

    def __init__(self, railroad):
        super().__init__()
        self.setStyleSheet("background-color: lightpink;")

        self.railroad = railroad

        size_x = 480
        size_y = 400

        self.setFixedSize(QSize(size_x, size_y))
        self.setWindowTitle("Railway")

        self.nodes_state = self.init_button('Stations', 120, 40, 0, 0, self.the_nodes_state_was_clicked)
        self.nodes = StationState(self, self.railroad[0].nodes, 'Stations')

        self.edges_state = self.init_button('Ways', 120, 40, 0, 50, self.the_edges_state_was_clicked)
        self.edges = WaysState(self, self.railroad[0].nodes, self.railroad[0].edges, 'Ways')

        self.railway_state = self.init_button('Railway', 120, 40, 0, 100, self.the_railway_state_was_clicked)
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Railway')

        self.trains_state = self.init_button('Trains', 120, 40, 0, 150, self.the_trains_state_was_clicked)
        self.trains = TrainsState(self, self.railroad[0].trains, 'Trains')

        self.add_station_button = self.init_button('Add station', 200, 40, 140, 0,
                                                   self.the_add_station_button_was_clicked)
        self.add_station = AddStation(self)

        self.add_way_stations_button = self.init_button('Add way', 200, 40, 140, 50,
                                                        self.the_add_way_stations_button_was_clicked)
        self.add_way_stations = AddWayStation(self)

        self.add_train_button = self.init_button('Add train', 200, 40, 140, 100,
                                                 self.the_add_train_button_was_clicked)
        self.add_train = AddTrain(self)

        self.add_goods_train_button = self.init_button('Add goods to train ', 200, 40, 140, 150,
                                                       self.the_add_goods_train_button_was_clicked)
        self.add_goods_train = AddGoodsTrain(self)

        self.add_goods_station_button = self.init_button('Add goods on station', 200, 40, 140, 200,
                                                         self.the_add_goods_station_button_was_clicked)
        self.add_goods_station = AddGoodsStation(self)

        self.add_goods_train_from_station_button = self.init_button('Add goods to train(station)', 200, 40, 140,
                                                                    250,
                                                                    self.the_add_goods_train_from_station_button_was_clicked)
        self.add_goods_train_from_station = AddGoodsTrainFromStation(self)

        self.remove_way_stations = RemoveWayStation(self)
        self.remove_way_stations_button = self.init_button('Remove way', 120, 40, 360, 0,
                                                           self.the_remove_way_stations_button_was_clicked)

        self.remove_station_button = self.init_button('Remove station', 120, 40, 360, 50,
                                                      self.the_remove_station_button_was_clicked)
        self.remove_station = RemoveStation(self)

        self.remove_train_button = self.init_button('Remove train', 120, 40, 360, 100,
                                                    self.the_remove_train_button_was_clicked)
        self.remove_train = RemoveTrain(self)

        self.save_button = self.init_button('Save', 120, 40, 180, 300,
                                                 self.the_time_move_button_was_clicked)

        self.time_move_button = self.init_button('Move', 120, 40, 180, 350,
                                                 self.the_time_move_button_was_clicked)


        self.add_station.submitClicked.connect(self.append_station)
        self.add_train.submitClicked.connect(self.append_train)
        self.add_way_stations.submitClicked.connect(self.append_way_stations)
        self.add_goods_train.submitClicked.connect(self.append_goods_train)
        self.add_goods_station.submitClicked.connect(self.append_goods_station)
        self.add_goods_train_from_station.submitClicked.connect(self.append_goods_train_from_station)
        self.remove_way_stations.submitClicked.connect(self.del_way_stations)
        self.remove_station.submitClicked.connect(self.del_station)
        self.remove_train.submitClicked.connect(self.del_train)
        self.time_move_button.setStyleSheet("background-color: orange;")
        self.save_button.setStyleSheet("background-color: orange;")

    def the_nodes_state_was_clicked(self):
        self.nodes.show()

    def the_edges_state_was_clicked(self):
        self.edges.show()

    def the_railway_state_was_clicked(self):
        self.railway.show()

    def the_trains_state_was_clicked(self):
        self.trains.show()

    def the_add_station_button_was_clicked(self):
        self.add_station.show()

    def the_add_train_button_was_clicked(self):
        self.add_train.show()

    def the_add_way_stations_button_was_clicked(self):
        self.add_way_stations.show()

    def the_add_goods_train_button_was_clicked(self):
        self.add_goods_train.show()

    def the_add_goods_train_from_station_button_was_clicked(self):
        self.add_goods_train_from_station.show()

    def the_add_goods_station_button_was_clicked(self):
        self.add_goods_station.show()

    def the_remove_way_stations_button_was_clicked(self):
        self.remove_way_stations.show()

    def the_remove_station_button_was_clicked(self):
        self.remove_station.show()

    def the_remove_train_button_was_clicked(self):
        self.remove_train.show()

    def the_time_move_button_was_clicked(self):
        self.railroad[0].time_move()
        self.nodes = StationState(self, self.railroad[0].nodes, 'Stations')
        self.trains = TrainsState(self, self.railroad[0].trains, 'Trains')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Railway')

    def append_station(self, station):
        self.railroad[0].append_station(station)
        self.nodes = StationState(self, self.railroad[0].nodes, 'Stations')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Railway')

    def append_train(self, temp_list):
        self.railroad[0].append_train(temp_list[1], temp_list[0])
        self.trains = TrainsState(self, self.railroad[0].trains, 'Trains')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Railway')

    def append_way_stations(self, temp_list):
        self.railroad[0].append_way_between_stations(temp_list[0], temp_list[1], temp_list[2])
        self.edges = WaysState(self, self.railroad[0].nodes, self.railroad[0].edges, 'Ways')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Railway')

    def append_goods_train(self, temp_list):
        self.railroad[0].append_goods_train(temp_list[0], temp_list[2], temp_list[1])
        self.trains = TrainsState(self, self.railroad[0].trains, 'Trains')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Railway')

    def append_goods_station(self, temp_list):
        self.railroad[0].append_goods_station(temp_list[0], temp_list[1])
        self.nodes = StationState(self, self.railroad[0].nodes, 'Stations')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Railway')

    def append_goods_train_from_station(self, train_index):
        self.railroad[0].append_goods_train_from_station(train_index)
        self.trains = TrainsState(self, self.railroad[0].trains, 'Trains')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Railway')

    def del_way_stations(self, temp_list):
        self.railroad[0].remove_way_between_stations(temp_list[0], temp_list[1])
        self.edges = WaysState(self, self.railroad[0].nodes, self.railroad[0].edges, 'Ways')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Railway')

    def del_station(self, station_name):
        self.railroad[0].remove_station(station_name)
        self.trains = TrainsState(self, self.railroad[0].trains, 'Trains')
        self.nodes = StationState(self, self.railroad[0].nodes, 'Stations')
        self.edges = WaysState(self, self.railroad[0].nodes, self.railroad[0].edges, 'Ways')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Railway')

    def del_train(self, train_index):
        self.railroad[0].remove_train(train_index)
        self.trains = TrainsState(self, self.railroad[0].trains, 'Trains')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Railway')