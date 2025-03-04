import sys

from PySide6 import QtCore, QtGui, QtWidgets

from application_login.login import LoginForm
from persons.add_person import AddPerson
from sample_app.UI.ui_main_window import Ui_mw_Main


class MainWindow(QtWidgets.QMainWindow, Ui_mw_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_Quit.triggered.connect(self.close)
        self.action_AddPerson.triggered.connect(self.open_add_person)

        self.login_form = LoginForm()
        self.login_form.login_successful.connect(self.show)
        self.login_form.show()

    @QtCore.Slot()
    def open_add_person(self):
        add_person = AddPerson()
        add_person.exec()
        add_person.show()


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    _main_window = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
