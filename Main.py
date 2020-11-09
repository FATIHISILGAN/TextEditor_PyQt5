import sys
from PyQt5 import *
from PyQt5.QtWidgets import QToolBox,QColorDialog, QSpinBox, QFontComboBox, QMessageBox, QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QMainWindow, QTextEdit, QCheckBox, QFileDialog, QInputDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Form(QWidget):

    def __init__(self):
        super().__init__()
        self.SetScreen()

        self.GetItems()

    def SetScreen(self):
        self.setWindowTitle("Işılgan Metin Editör")
        self.resize(700,500)
        sshFile="style.css"
        with open(sshFile,"r") as fh:
             
            self.setStyleSheet(fh.read())
        
        

    def GetItems(self):
        layout = QGridLayout()
        #rich
        self.richText = QTextEdit()
        self.richText.textChanged.connect(self.richText_changed)
        #rich

        #save
        save = QPushButton()
        save.setIcon(QIcon("iconlar/save.png"))

        save.clicked.connect(self.save_clicked)
        save.setFixedSize(80,20)
        #save

        #opentext
        opentext = QPushButton()
        opentext.setIcon(QIcon("iconlar/open.png"))
        opentext.clicked.connect(self.opentext_clicked)
        opentext.setFixedSize(80,20)
        #opentext

        #fontSet
        self.fontCombo = QFontComboBox()

        self.fontCombo.activated.connect(self.fontSelect)
        self.fontCombo.setFixedSize(150,20)
        #fontSet

        #fontSize
        self.spiner = QSpinBox()
        self.spiner.valueChanged.connect(self.sizeSelect)
        self.spiner.setFixedSize(130,20)

        #fontSize

        #colorSelect
        self.colorButton = QPushButton()
        self.colorButton.setIcon(QIcon("iconlar/color.png"))
        self.colorButton.clicked.connect(self.colorButton_clicked)
        self.colorButton.setFixedSize(50,20)

        #colorSelect

        #Addimage
        self.addImage = QPushButton()
        self.addImage.clicked.connect(self.addImage_clicked)
        self.addImage.setIcon(QIcon("iconlar/add.png"))
        self.addImage.setFixedSize(30,20)
        #Addimage

        #FindWord
        self.findWord=QPushButton()
        self.findWord.setIcon(QIcon("iconlar/find.png"))
        self.findWord.clicked.connect(self.findWord_clicked)
        self.findWord.setFixedSize(30,20)
        
        #FindWord
 
        #hizalamaveBoldİtalicMenuOpen
        self.widg1=QWidget()
        self.widg2=QWidget()
        

        self.toolBox=QToolBox()
        self.toolBox.setFixedSize(150,300)

     

        self.ortala=QPushButton()
        self.ortala.setFixedSize(30,40)
        self.ortala.setIcon(QIcon("iconlar/center"))
        self.sağyasla=QPushButton()
        self.sağyasla.setIcon(QIcon("iconlar/right.png"))
        self.sağyasla.setFixedSize(30,40)
        self.solaYasla=QPushButton()
        self.solaYasla.setIcon(QIcon("iconlar/left.png"))
        self.solaYasla.setFixedSize(30,40)
        self.ikiyanayasla=QPushButton()
        self.ikiyanayasla.setIcon(QIcon("iconlar/justify_align.png"))
        self.ikiyanayasla.setFixedSize(30,40)
        self.bold=QPushButton()
        self.bold.setFixedSize(30,40)
        self.bold.setIcon(QIcon("iconlar/Bold.png"))
        self.italic=QPushButton()
        self.italic.setIcon(QIcon("iconlar/italic.png"))
        self.italic.setFixedSize(30,40)
      

        self.layoutHizalama=QGridLayout()
        self.layoutHizalama.addWidget(self.ortala,0,0)
        self.layoutHizalama.addWidget(self.sağyasla,1,0)
        self.layoutHizalama.addWidget(self.solaYasla,2,0)
        self.layoutHizalama.addWidget(self.ikiyanayasla,3,0)



        self.layoutBoldİtalic=QGridLayout()
        self.layoutBoldİtalic.addWidget(self.bold,0,0)
        self.layoutBoldİtalic.addWidget(self.italic,1,0)



        self.widg1.setLayout(self.layoutHizalama)
        self.widg2.setLayout(self.layoutBoldİtalic)


        self.toolBox.addItem(self.widg1,"hizalamalar")
        self.toolBox.addItem(self.widg2,"Yazı biçimleri")
        #hizalamaBoldİtalicMenuOpen



        
        

        layout.addWidget(save, 5,1 )
        layout.addWidget(self.richText, 0, 0,-1,1)
        layout.addWidget(opentext, 6, 1)
        layout.addWidget(self.spiner, 4, 1)
        layout.addWidget(self.fontCombo, 3, 1)
        layout.addWidget(self.colorButton, 7, 1)
        layout.addWidget(self.addImage, 8, 1) 
        layout.addWidget(self.findWord, 9, 1)  
        layout.addWidget(self.toolBox,10,1)







        self.setLayout(layout)
    def richText_changed(self):
        text = self.richText.toPlainText()
      

        
        temp=0
       
        for i in text.split(" "):

            temp = temp+1

            

              
        self.setWindowTitle(str(temp))   
    def findWord_clicked(self):
      


        aranan, onay = QInputDialog.getText(
                self, " aranan kelimeyi giriniz:", "kelime bul")
        
        text = self.richText.toPlainText()
      

        count = 0
        temp=0
       
        for line in text.split(" "):

            



            temp=temp+1
           
             
           
            if line==aranan:
               
                count = count+1
                QMessageBox.about(self, "bul", str(temp)+".sıradaki kelime aradığınız kelimedir")
        QMessageBox.about(self, "bul", str(count)+" adet bulundu ")
        
        

    def addImage_clicked(self):
        imagePath = QFileDialog.getOpenFileName(self, 'Open file')
        document = self.richText.document()
        cursor = QTextCursor(document)
        cursor.insertImage(imagePath[0])
        #getopenfilename tupple döndürdüğü için ve 0.indexde path olduğu için 0.indexi verdik

    def colorButton_clicked(self):
        color = QColorDialog.getColor()
        self.richText.setTextColor(color)

    def sizeSelect(self):
        self.richText.setFontPointSize(self.spiner.value())

    def fontSelect(self):
        self.richText.setFont(self.fontCombo.currentFont())

    def opentext_clicked(self):

        filename = QFileDialog.getOpenFileName(self, 'Open File')

        if filename[0]:

            f = open(filename[0], 'r')

            with f:

               data = f.read()
               self.richText.setText(data)

    def save_clicked(self):
        try:
            fname = QFileDialog.getExistingDirectory(self, 'Open f', '/home')

            metin, onay = QInputDialog.getText(
                self, " dosyanın adını giriniz", "dosya adı:")

            metinuzantı, onay = QInputDialog.getText(
                self, " dosyanın uzantısını giriniz", "dosya uzantısı:")
            metinad = ""
            uzantıad = ""
            if onay == True:

                metinad = metin
                uzantıad = metinuzantı

            with open(fname+"/"+metinad+"."+uzantıad, 'w') as f:
                my_text = self.richText.toPlainText()
                f.write(my_text)
            QMessageBox.about(self, "Bilgilendirme", "Başarı ile kaydedildi")
        except:
            QMessageBox.about(self, "Runtime ERROR", "Birşey oldu")


if __name__ == "__main__":

    app = QApplication(sys.argv)
                       
    form1 = Form()
                           
    form1.show()
    sys.exit(app.exec_())
app()
