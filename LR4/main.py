import Commands
import RailRoadFile
import sys
from PyQt6.QtWidgets import QApplication
import App
import Test


def main():
    railroad = [RailRoadFile.RailRoad([], {}, [])]
    railroad[0] = Test.rail
    is_app = input('----------------------------------gui or cli------------------------------------\n').lower()
    if is_app == 'gui':
        app = QApplication(sys.argv)

        window = App.MainWindow(railroad)
        window.show()

        app.exec()
    elif is_app == 'cli':
        print('input command')
        while True:
            session_ended = Commands.get_command(railroad)
            if session_ended:
                break


if __name__ == '__main__':
    main()