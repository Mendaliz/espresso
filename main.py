import sys

from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QApplication


class SqlCoffee(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()

        model = QSqlTableModel(self, db)
        model.setTable('Coffee')
        model.select()

        self.view.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SqlCoffee()
    ex.show()
    sys.exit(app.exec())


