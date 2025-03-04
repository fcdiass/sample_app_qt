import sys

from PySide6 import QtCore, QtGui, QtWidgets

from application_login.UI.ui_login_window import Ui_w_LoginForm


class LoginForm(QtWidgets.QWidget, Ui_w_LoginForm):
    login_successful = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_Cancel.clicked.connect(self.close)
        self.pb_OK.clicked.connect(self.process_login)
        self.pb_OK.setAutoDefault(True)
        self.pb_Cancel.setAutoDefault(True)

    @QtCore.Slot()
    def process_login(self):
        if self.le_UserID.text() == "admin" and self.le_Password.text() == "admin":
            self.login_successful.emit()
            self.close()
        else:
            self.lb_Message.setText("Invalid User ID or Password")


def main():
    app = QtWidgets.QApplication(sys.argv)
    login_form = LoginForm()
    login_form.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
