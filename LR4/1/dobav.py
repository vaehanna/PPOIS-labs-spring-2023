from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class AddStation(QMainWindow):
    submitClicked = pyqtSignal(str)

    def __init__(self, parent=None):
        super(AddStation, self).__init__(parent)

        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("Add station")

        self.lable_station_name = QLabel(self)
        self.lable_station_name.setText('Station name: ')

        self.station_name_line = QLineEdit(self)
        self.station_name_line.move(110, 0)

        self.button = QPushButton('Add station', self)
        self.button.resize(120, 40)
        self.button.move(150, 200)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        self.submitClicked.emit(self.station_name_line.text())
        self.station_name_line.clear()
        self.close()


class AddTrain(QMainWindow):
    submitClicked = pyqtSignal(list)

    def __init__(self, parent=None):
        super(AddTrain, self).__init__(parent)

        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("Add train")

        self.lable_station_name = QLabel(self)
        self.lable_station_name.setText('Start station: ')

        self.station_name_line = QLineEdit(self)
        self.station_name_line.move(110, 0)

        self.lable_speed = QLabel(self)
        self.lable_speed.setText('Speed: ')
        self.lable_speed.move(0, 40)

        self.speed_line = QLineEdit(self)
        self.speed_line.move(110, 40)

        self.button = QPushButton('Add train', self)
        self.button.resize(120, 40)
        self.button.move(150, 200)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        self.submitClicked.emit([self.station_name_line.text(), int(self.speed_line.text())])
        self.station_name_line.clear()
        self.speed_line.clear()
        self.close()


class AddWayStation(QMainWindow):
    submitClicked = pyqtSignal(list)

    def __init__(self, parent=None):
        super(AddWayStation, self).__init__(parent)

        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("Add way")

        self.lable_station1_name = QLabel(self)
        self.lable_station1_name.resize(150, 40)
        self.lable_station1_name.setText('1st station name: ')

        self.station1_name_line = QLineEdit(self)
        self.station1_name_line.move(160, 0)

        self.lable_station2_name = QLabel(self)
        self.lable_station2_name.move(0, 40)
        self.lable_station2_name.resize(150, 40)
        self.lable_station2_name.setText('2nd station name: ')

        self.station2_name_line = QLineEdit(self)
        self.station2_name_line.move(160, 40)

        self.lable_distance = QLabel(self)
        self.lable_distance.move(0, 80)
        self.lable_distance.setText('Distance: ')

        self.distance_line = QLineEdit(self)
        self.distance_line.move(160, 80)

        self.button = QPushButton('Add way', self)
        self.button.resize(120, 40)
        self.button.move(150, 200)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        self.submitClicked.emit(
            [self.station1_name_line.text(), self.station2_name_line.text(), int(self.distance_line.text())])
        self.station1_name_line.clear()
        self.station2_name_line.clear()
        self.distance_line.clear()
        self.close()


class AddGoodsTrain(QMainWindow):
    submitClicked = pyqtSignal(list)

    def __init__(self, parent=None):
        super(AddGoodsTrain, self).__init__(parent)

        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("Add goods")

        self.lable_station_name = QLabel(self)
        self.lable_station_name.setText('Destination: ')

        self.station_name_line = QLineEdit(self)
        self.station_name_line.move(110, 0)

        self.lable_goods = QLabel(self)
        self.lable_goods.move(0, 40)
        self.lable_goods.setText('Goods: ')

        self.goods_line = QLineEdit(self)
        self.goods_line.move(110, 40)

        self.lable_num_train = QLabel(self)
        self.lable_num_train.move(0, 80)
        self.lable_num_train.setText('Train number: ')

        self.num_train_line = QLineEdit(self)
        self.num_train_line.move(110, 80)

        self.button = QPushButton('Add goods', self)
        self.button.resize(120, 40)
        self.button.move(150, 200)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        self.submitClicked.emit(
            [self.station_name_line.text(), self.goods_line.text(), int(self.num_train_line.text())])
        self.station_name_line.clear()
        self.goods_line.clear()
        self.num_train_line.clear()
        self.close()


class AddGoodsStation(QMainWindow):
    submitClicked = pyqtSignal(list)

    def __init__(self, parent=None):
        super(AddGoodsStation, self).__init__(parent)

        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("Add goods")

        self.lable_station_name = QLabel(self)
        self.lable_station_name.setText('Destination: ')

        self.station_name_line = QLineEdit(self)
        self.station_name_line.move(110, 0)

        self.lable_goods = QLabel(self)
        self.lable_goods.move(0, 40)
        self.lable_goods.setText('Goods: ')

        self.goods_line = QLineEdit(self)
        self.goods_line.move(110, 40)

        self.button = QPushButton('Add goods', self)
        self.button.resize(120, 40)
        self.button.move(150, 200)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        self.submitClicked.emit(
            [self.station_name_line.text(), self.goods_line.text()])
        self.station_name_line.clear()
        self.goods_line.clear()
        self.close()


class AddGoodsTrainFromStation(QMainWindow):
    submitClicked = pyqtSignal(int)

    def __init__(self, parent=None):
        super(AddGoodsTrainFromStation, self).__init__(parent)

        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("Add goods on train")

        self.lable_num_train = QLabel(self)
        self.lable_num_train.setText('Train number: ')

        self.num_train_line = QLineEdit(self)
        self.num_train_line.move(100, 0)

        self.button = QPushButton('Add goods', self)
        self.button.resize(120, 40)
        self.button.move(150, 200)
        self.button.clicked.connect(self.the_button_was_clicked)



    def the_button_was_clicked(self):
        self.submitClicked.emit(int(self.num_train_line.text()))
        self.num_train_line.clear()
        self.close()