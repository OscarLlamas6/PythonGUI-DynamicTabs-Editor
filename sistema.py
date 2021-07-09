import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui, Qsci
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *
from os import *
from PyQt5.Qsci import *
import io
import os

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class iniciar():
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("vprincipal.ui")
        self.__myFont = QFont()
        self.archivo = ""
        self.lenguaje = ""
        self.__myFont.setPointSize(14)
        self.ventana.__editor = QsciScintilla()
        self.ventana.__editor.setUtf8(True) 
        self.ventana.__editor.setFont(self.__myFont) 
        self.ventana.__editor.setMarginType(0, QsciScintilla.NumberMargin)
        self.ventana.__editor.setMarginWidth(0, "000")
        self.ventana.__editor.setMarginsForegroundColor(QColor("#56ff00"))
        self.ventana.__editor.setMarginsBackgroundColor(QColor("#000000"))
        self.__lexer = QsciLexerJava(self.ventana.__editor)
        self.ventana.__editor.setLexer(self.__lexer)
        self.ventana.verticalLayout.addWidget(self.ventana.__editor)
        self.ventana.actionNueva_pesta_a.triggered.connect(self.insertTab)
        self.ventana.actionEliminar_pesta_a.triggered.connect(self.removeTab)
        self.ventana.actionAnalizar.triggered.connect(self.getText)
        self.ventana.actionAbrir.triggered.connect(self.abrir)
        self.ventana.actionAcerca_de.triggered.connect(self.acerca)
        self.ventana.actionGuardar.triggered.connect(self.guardar)
        self.ventana.actionGuardar_Como.triggered.connect(self.guardarComo)
        self.ventana.actionSalir.triggered.connect(self.salir)
        self.ventana.editores = []
        self.ventana.editores.append(self.ventana.__editor)
        self.ventana.show()
        app.exec()
        
    def getText(self):
        contenido = self.ventana.editores[self.ventana.tabWidget.currentIndex()].text()
        print(contenido)
            
    def abrir(self):
        global archivo
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        openF, _ = QFileDialog.getOpenFileName(self.ventana,"Abrir archivo", "" ,"All Files (*);;Python Files (*.py)", options=options)
        if openF != "":
            archivo = openF
            print("el archivo elegido fue: ",archivo)
            entrada = io.open(archivo, encoding="utf-8")
            contenido = entrada.read()
            self.ventana.editores[self.ventana.tabWidget.currentIndex()].setText(contenido)
            entrada.close()
    
    def guardar(self):
        global archivo
        if archivo == "":
            self.guardarComo()
        else:
            guardarc = io.open(archivo, "w", encoding="utf-8")
            guardarc.write(self.ventana.editores[self.ventana.tabWidget.currentIndex()].text())
            guardarc.close()
    
    def guardarComo(self):
        global archivo
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        guardar, _ = QFileDialog.getSaveFileName(self.ventana,"Guardar como...", "", "All Files (*);;Python Files (*.py)", options=options)
        if guardar != "":
            fguardar = io.open(guardar, "w+", encoding="utf-8")
            fguardar.write(self.ventana.editores[self.ventana.tabWidget.currentIndex()].text())
            fguardar.close()
            archivo = guardar
    
    def acerca(self):
        QMessageBox.about(self.ventana, "Acerca de:", "Autor: Oscar Alfredo Llamas Lemus\n")
        
    def insertTab(self):
        tab = QtWidgets.QWidget()
        frame = QtWidgets.QFrame(tab)
        frame.setGeometry(QtCore.QRect(0, 0, 1021, 581))
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        verticalLayoutWidget = QtWidgets.QWidget(frame)
        verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1031, 581))
        verticalLayout = QtWidgets.QVBoxLayout(verticalLayoutWidget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        __editor = QsciScintilla()
        __editor.setUtf8(True) 
        __editor.setFont(self.__myFont) 
        __editor.setMarginType(0, QsciScintilla.NumberMargin)
        __editor.setMarginWidth(0, "000")
        __editor.setMarginsForegroundColor(QColor("#56ff00"))
        __editor.setMarginsBackgroundColor(QColor("#000000"))
        __lexer = QsciLexerJava(__editor)
        __editor.setLexer(self.__lexer)
        verticalLayout.addWidget(__editor)   
        self.ventana.tabWidget.addTab(tab, "new")
        self.ventana.editores.append(__editor)
        self.renameTabs()
        self.ventana.tabWidget.setCurrentWidget(self.ventana.tabWidget.widget(self.ventana.tabWidget.count()-1))
              
    def removeTab(self):
        if self.ventana.tabWidget.count() > 1 :
            self.ventana.tabWidget.removeTab(self.ventana.tabWidget.currentIndex())
            self.ventana.editores.pop(self.ventana.tabWidget.currentIndex())
            self.renameTabs()
        else:
            sys.exit()
    
    def renameTabs(self):
        n = self.ventana.tabWidget.count()
        for x in range(0, n):
            self.ventana.tabWidget.setTabText(x, "Tab "+ str(x+1))
        
        #sys.exit()

    def salir(self):
        sys.exit()

suppress_qt_warnings()
iniciar()