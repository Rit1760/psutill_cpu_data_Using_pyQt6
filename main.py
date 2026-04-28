
from PyQt6 import QtCore, QtWidgets, QtGui
import sys
import psutil
import pyqtgraph as pg

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle("CPU Monitor")
        self.setGeometry(100, 100, 600, 400)

        self.setWindowIcon(QtGui.QIcon("VNT-logo.png"))

        self.setStyleSheet("""
            background-color: #f0f0f0;
            font-family: Arial;
            font-size: 14px;
        """)

     
        central_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

      
        self.cpu_label = QtWidgets.QLabel("CPU Usage: 0%")
        self.cpu_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.cpu_label)

       
        self.graph = pg.PlotWidget()
        self.graph.setTitle("CPU Usage Graph")
        self.graph.setYRange(0, 100)
        layout.addWidget(self.graph)

  
        self.x = list(range(100))   
        self.y = [0] * 100        
        self.line = self.graph.plot(self.x, self.y)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)

    def update_data(self):
        cpu = psutil.cpu_percent()

        self.cpu_label.setText(f"CPU Usage: {cpu}%")

        self.y = self.y[1:] + [cpu]
        self.line.setData(self.x, self.y)



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
