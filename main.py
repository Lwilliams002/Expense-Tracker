from PyQt5.QtWidgets import QApplication
from app.views.main_window import MainWindow
import sys
import resources

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())