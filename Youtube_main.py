from PyQt5.QtWidgets import *
from Youtube_bitti_4 import Ui_MainWindow
from pytube import YouTube,Playlist
import webbrowser
from threading import Thread
import sqlite3
from indirilen import  Quest
from indirilen_ui import Ui_Database
from PyQt5 import QtGui
import os

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.database = Ui_Database()

        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.dosya_yukle)
        self.ui.comboBox.currentTextChanged.connect(self.resolution)

        self.ui.action_ndirilenler_listesi.triggered.connect(self.indirilen_goster)
        self.ui.pushButton_4.clicked.connect(self.github_yonlendir)
        self.ui.pushButton_3.clicked.connect(self.github_yonlendir)
        self.ui.pushButton_2.clicked.connect(self.videoYukle_Th)
        self.ui.radioButton_2.setChecked(True)
        self.conn = sqlite3.connect("audio1.db")
        self.cursor =self.conn.cursor()

        self.cursor.execute("Create Table IF NOT EXISTS audio1 (liste TEXT,liste2 TEXT)")

    def github_yonlendir(self):
        url = "https://github.com/BerkeGokturk71"
        webbrowser.open_new_tab(url)
    def resolution(self):
        pass


    def videoYukle_Th(self):
        Thread(target=self.audio).start()


    def audio(self):
        self.url =  self.ui.lineEdit.text()
        self.conn = sqlite3.connect("audio1.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("Create Table IF NOT EXISTS audio1 (liste TEXT,liste2 TEXT)")
        try:  ## Hata varmı kontrol ediyoruz
            video = YouTube(self.url)  ## Hata yok ise video değişkenini YouTube(bağlantıAdresi) fonksiyonu olarak atıyoruz
            self.ui.label_3.setText(f"{video.title} Adlı video indirilmeye başlandı.")

            if self.ui.radioButton_2.isChecked():
                ayrilmis = video.streams.filter(only_audio=True).all()
                print(ayrilmis)
                base, ext = os.path.splitext(ayrilmis[1].download(self.file_dialog_yukle))
                new_file = base + '.mp3'
                os.rename(ayrilmis[3].download(self.file_dialog_yukle), new_file)


                liste = []
                liste.append(video.title)
                self.cursor.execute("INSERT INTO audio1 (liste,liste2) VALUES (?,?)", (liste[0], liste[0]))
                self.conn.commit()

                self.ui.label_3.setText(
                    f"{video.title} Adlı video başarılı bir şekilde indirildi.")  ## İndirme tamamlandı yazdırıyoruz

            else:
                p = Playlist(self.url)

                for videolist in p.videos:
                    ayrilmis = videolist.streams.filter(only_audio=True).all()
                    print(ayrilmis)
                    base, ext = os.path.splitext(ayrilmis[1].download(self.file_dialog_yukle))
                    new_file = base + '.mp3'
                    os.rename(ayrilmis[1].download(self.file_dialog_yukle), new_file)

                    liste = []
                    liste.append(videolist.title)
                    self.cursor.execute("INSERT INTO audio1 (liste,liste2) VALUES (?,?)", (liste[0], liste[0]))
                    self.conn.commit()

                    self.ui.label_3.setText(f"{videolist.title} Adlı video başarılı bir şekilde indirildi.")  ## İndirme tamamlandı yazdırıyoruz



            self.ui.label_3.setText("Bütün indirme islemleri tamamlandı ;)")

        except:  ## Sorun var ise
            self.ui.label_3.setText("İşlem esnasında bir sorun ile karşılaşıldı!")  ## Ekrana hata var yazdırıyoruz


    def dosya_yukle(self):
        #file_dialog = QFileDialog().getOpenFileName(self,"Open File (*)",)
        file_dialog = QFileDialog()
        self.file_dialog_yukle = file_dialog.getExistingDirectory(self, "Select")# dosyayı seçtik
        self.konum_list = []
        self.konum_list.append(self.file_dialog_yukle)
        self.ui.statusBar.showMessage(f"{self.konum_list[0]} Adlı Klasor Secildi", 3000)
        print(self.konum_list)
          # labele yazdırdık

    def indirilen_goster(self):

        self.indir = Quest()
        self.indir.show()


uygulama  = QApplication([])
ekran = Window()
ekran.setWindowTitle("Youtube Converter")
ekran.setWindowIcon(QtGui.QIcon('Main.png'))
ekran.show()
uygulama.exec()