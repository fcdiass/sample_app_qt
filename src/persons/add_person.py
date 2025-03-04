import sys

from PySide6 import QtCore, QtGui, QtWidgets

from persons.UI.ui_add_person_window import Ui_d_person


class AddPerson(QtWidgets.QDialog, Ui_d_person):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lb_Message.clear()
        self.pb_Close.clicked.connect(self.reject)

        self.pb_Submit.clicked.connect(self.process_entry)

    @QtCore.Slot()
    def process_entry(self):
        self.lb_Message.setText("Person Added Successfully")
        self.le_FristName.clear()
        self.le_LastName.clear()
        self.le_FristName.setFocus()


def main():
    app = QtWidgets.QApplication(sys.argv)
    add_person = AddPerson()
    add_person.open()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
