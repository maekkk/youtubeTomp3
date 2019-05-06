import os
from pytube import YouTube
import tkinter, tkinter.filedialog, tkinter.messagebox

class Downloader:
  def __init__(self, url):
    self.yt = YouTube(url)
    self.getStream()

  def getStream(self):
    list = self.yt.streams.filter(progressive=True).all()
    for i, j in enumerate(list):
      print('[{0}]:{1}'.format(i, j))

    #targetNo = int(input("Enter Stream# : "))
    targetNo = 0
    self.targetStream = list[targetNo]
    self.yt.register_on_progress_callback(self.progress)
    self.targetStream.download()


  def progress(self, stream, chunk, file_handle, bytes_remaining):
    p = file_handle.tell()/(file_handle.tell()+bytes_remaining)*100
    print(p,'%')


class Converter:
  def __init__(self, filename):
    self.filename = filename
    self.root, self.ext = os.path.splitext(self.filename)
    self.convToMp3()

  def convToMp3(self):
    convcmd = "ffmpeg -i {} -y {}".format("\""+self.filename+"\"", "\""+self.root+"\""+".mp3")
    os.system(convcmd)

    #delfile = input("Delete the movie file? y/n: ")
    #if delfile == "y":
    self.delete()

  def delete(self):
      delcmd = "del {}".format("\""+self.filename+"\"")
      os.system(delcmd)




if __name__ == "__main__":
    #読み込みファイルの指定
    root = tkinter.Tk()
    root.withdraw()
    fTyp = [("","*.txt")]
    iDir = os.path.abspath(os.path.dirname(__file__))
#    tkinter.messagebox.showinfo('○×プログラム','処理ファイルを選択してください！')
    file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

    print  (file)
    #ファイルの読み込み
    f = open(file)
    lines2 = f.readlines()
    # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    f.close()
    # lines2: リスト。要素は1行の文字列データ
    for line in lines2:
        print (line)
        d = Downloader(line)
        c = Converter(d.targetStream.default_filename)


#   url = input("Enter YouTube Video URL txt : ")
#   print  (url)
#  url = input("Enter YouTube Video URL : ")
#  d = Downloader(url)
#  c = Converter(d.targetStream.default_filename)
