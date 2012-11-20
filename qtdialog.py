
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    def __init__(self,app,img):
        QtGui.QWidget.__init__(self)

        self.mainApp = app;

        self.buttonY = QtGui.QPushButton('Yes', self)
        self.buttonY.clicked.connect(self.handleButtonY)

        self.buttonN = QtGui.QPushButton('No', self)
        self.buttonN.clicked.connect(self.handleButtonN)

        self.view = QtGui.QGraphicsView()
        self.scene = QtGui.QGraphicsScene()
        self.scene.addPixmap(QtGui.QPixmap(img))
        self.view.setScene(self.scene)
        
        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.view,0,0,1,2)
        layout.addWidget(self.buttonY,1,0)
        layout.addWidget(self.buttonN,1,1)


    def handleButtonY(self):
        app.exit(1)

    def handleButtonN(self):
        app.exit(2)

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    if not len(sys.argv)>1:
        sys.exit(-1)
    window = Window(app,sys.argv[1])
    window.show()
    sys.exit(app.exec_())
