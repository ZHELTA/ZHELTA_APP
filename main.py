from ast import Import
import sys
from PySide6 import QtCore, QtWidgets, QtGui
import json


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1680,720)
        self.setFixedHeight(720)
        self.setMinimumWidth(800)
        self.setWindowTitle("ZHELTA APP")
        self.setWindowIcon(QtGui.QIcon("icons/icon.ico"))
        self.setStyleSheet("background-color: #17181A")
        
        self.createTabs()
        
        self.show()

    def createTabs(self):
        layout = QtWidgets.QVBoxLayout()
        tabs = QtWidgets.QTabWidget()
        tabs.addTab(self.importTabUI(),"Import")
        tabs.addTab(self.keyMapTabUI(),"KeyMap")
        tabs.addTab(self.willBeSoon(),"Macros")
        tabs.addTab(self.willBeSoon(),"OLED")
        tabs.addTab(self.willBeSoon(),"Key tester")
        tabs.addTab(self.willBeSoon(),"Settings")
        layout.addWidget(tabs)
        self.setLayout(layout)
        

    def importTabUI(self):
        gridFrame = QtWidgets.QFrame(self)
        gridFrame.setStyleSheet("background-color: #222326;")
        nestedLayout = QtWidgets.QVBoxLayout()
        gridImportLayout = QtWidgets.QGridLayout()


        functionalImportLayout = QtWidgets.QVBoxLayout()
        buttonToImportJSONFile = QtWidgets.QPushButton("Import keyboard layout .JSON file")
        buttonToImportJSONFile.setStyleSheet("background-color: #222326; color: #E39417; max-width: 300px; min-height: 50px;")
        buttonToImportJSONFile.setCheckable(True)
        buttonToImportJSONFile.clicked.connect(lambda: self.isButtonToImportClicked(buttonToImportJSONFile, gridImportLayout))
        functionalImportLayout.addWidget(buttonToImportJSONFile, alignment=QtCore.Qt.AlignCenter)
        nestedLayout.addLayout(gridImportLayout)
        nestedLayout.addLayout(functionalImportLayout)
        gridFrame.setLayout(nestedLayout)
        return gridFrame

    def isButtonToImportClicked(self,checkButton, layout):
        getFileJSON = QtWidgets.QFileDialog.getOpenFileName(self,'Open JSON file', '.','*.json')
        with open(getFileJSON[0],'r') as file:
            data = file.read()
        jsonLoadsData = json.loads(data)
        for i in reversed(range(layout.count())): 
            layout.itemAt(i).widget().setParent(None)
        for i in jsonLoadsData:
            nameOfLayout = i['name']
            matrixOfLayout = i['matrix']
            layoutsOfLayout = i['layouts']
        print(nameOfLayout)
        checkButton.setText("Change file")
        checkButton.setChecked(False)
        for i in range(0,matrixOfLayout['rows']):
            for j in range(0,matrixOfLayout['cols']):
                bToKeyboard = QtWidgets.QPushButton("")
                bToKeyboard.setStyleSheet("height: 100px; border-width: 3px;")
                layout.addWidget(bToKeyboard,i,j)

    def willBeSoon(self):
        keyMapTab = QtWidgets.QWidget()
        keyMapTab.setStyleSheet("background-color: #222326;")
        keyMapLayout = QtWidgets.QVBoxLayout()
        labelInformationThatItWillBeAddedSoon = QtWidgets.QLabel()
        labelInformationThatItWillBeAddedSoon.setText("It will be added soon.")
        labelInformationThatItWillBeAddedSoon.setStyleSheet("font-size: 34px; color: #E39417; text-align:center;")
        labelInformationThatItWillBeAddedSoon.setAlignment(QtCore.Qt.AlignCenter)
        keyMapLayout.addWidget(labelInformationThatItWillBeAddedSoon)
        keyMapTab.setLayout(keyMapLayout)
        return keyMapTab


    def keyMapTabUI(self):
        keyMapFrame = QtWidgets.QFrame(self)
        keyMapFrame.setStyleSheet("background-color: #222326;")
        nestedKeyMapLayout = QtWidgets.QVBoxLayout()
        topKeyboardLayout = QtWidgets.QGridLayout()
        bottomUseKeysLayout = QtWidgets.QGridLayout()

        with open('allKeysLayout.json','r') as file:
            data = file.read()
        layoutNames = json.loads(data)

        positions = [(i, j) for i in range(2) for j in range(20)]
        

        for position, name in zip(positions, layoutNames):
         if name == '':
          continue
         button = QtWidgets.QPushButton(name)
         button.setStyleSheet("font-size: 18px; color: #E39417; text-align:center;")
         topKeyboardLayout.addWidget(button, *position)

        nestedKeyMapLayout.addLayout(topKeyboardLayout)
        nestedKeyMapLayout.addLayout(bottomUseKeysLayout)
        keyMapFrame.setLayout(nestedKeyMapLayout)
        return keyMapFrame

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    with open("mainqt.css","r") as file:
        app.setStyleSheet(file.read())

    sys.exit(app.exec())