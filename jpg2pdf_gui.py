#coding=utf-8
from PyQt4 import  QtCore, QtGui
import jpg2pdf
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
class Window( QtGui.QWidget ):
    def __init__( self ):
        super( Window, self ).__init__()
        self.setWindowTitle('jpg2pdf')
        self.resize( 300, 150 )
        gridlayout = QtGui.QGridLayout()
        label1 = QtGui.QLabel('this is a test version.you can select a floder and transform every picture there to pdf')
        gridlayout.addWidget(label1,0,0)
        self.button1 = QtGui.QPushButton('File')
        gridlayout.addWidget(self.button1)
        self.setLayout( gridlayout )
        self.connect( self.button1, QtCore.SIGNAL('clicked()'), self.OnButton1 )

    def OnButton1(self):
        fileName = QtGui.QFileDialog.getExistingDirectory( self, 'Open' )
        if not fileName.isEmpty():
            #print fileName
            jpg2pdf.topdf(str(fileName).decode('utf8','ignore'),pictureType=['png','jpg'])
            QtGui.QMessageBox.warning( self, "jpg2pdf", "complete", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No )

def main():
    app = QtGui.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec_()

if __name__ == '__main__':
    main()
