import sqlite3
from pytube import YouTube,Playlist

class berke:
    def __init__(self):
        self.conn = sqlite3.connect("audio1.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("Create Table  If Not EXISTS audio1 (liste TEXT,liste2 TEXT)")

        self.url = "https://www.youtube.com/watch?v=AUAAatNR7V4&list=PLXtKUs1gz6yaizEJMRigqEZ0z-5X9Lf8D&index=2&ab_channel=Pinhani"

        try:  ## Hata varmı kontrol ediyoruz
            video = YouTube( self.url)  ## Hata yok ise video değişkenini YouTube(bağlantıAdresi) fonksiyonu olarak atıyoruz
            print(f"{video.title} Adlı video indirilmeye başlandı.")


            ayrilmis = video.streams.filter(only_audio=True).all()
            ayrilmis[2].download("")
            print(f"{video.title} Adlı video başarılı bir şekilde indirildi.")  ## İndirme tamamlandı yazdırıyoruz

            '''
            for videolist in p.videos:
            ayrilmis = videolist.streams.filter(only_audio=True).all()
            ayrilmis[2].download("")
            print(f"{videolist.title} Adlı video başarılı bir şekilde indirildi.")  ## İndirme tamamlandı yazdırıyoruz
            '''


            self.cursor.execute("Select liste from audio1")
            indirilen_goster = self.cursor.fetchall()
            for i in indirilen_goster:
                print(i)



        except Exception:
            print("eroor")

berke()
