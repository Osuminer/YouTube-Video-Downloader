from pytube import YouTube
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import (QPixmap, QIcon)
import sys
import urllib

def Window():
    app = QApplication(sys.argv)
    win = QDialog()
    win.setWindowTitle("YouTube Video Downloader")
    win.setWindowIcon(QIcon("icon.png"))
    layout = QGridLayout()
    pixmap = QPixmap()


    # Search Button Click Function
    def searchButton_clicked():
        statusLabel.setText("Status: Searching")
        link = le.text()
        yt = YouTube(link)
        url = yt.thumbnail_url
        data = urllib.request.urlopen(url).read()
        pixmap.loadFromData(data)

        # Print Updated Video Data
        titleLabel.setText("Title:     {}".format(yt.title))
        authorLabel.setText("Author:  {}".format(yt.author))
        viewLabel.setText("Views:   {}".format(yt.views))
        lengthLabel.setText("Length:  {}sec".format(yt.length))
        thumbLabel.setPixmap(pixmap.scaledToHeight(100))

        statusLabel.setText("Status: Found")

        if audioButton.isChecked() == True:
            ys = yt.streams.get_audio_only()
        elif videoButton.isChecked() == True:
            ys = yt.streams.filter(only_video=True).order_by('resolution').last()
        elif bothButton.isChecked() == True:
            ys = yt.streams.get_highest_resolution()
        print(ys)
        return ys

    # Download Button Click Function
    def downButton_clicked():
        statusLabel.setText("Status: Downloading")
        ys = searchButton_clicked()
        location = locBox.text()
        ys.download(location)
        statusLabel.setText("Status: Download Completed")
  

    # Video Link Input
    le = QLineEdit()
    le.setText("Enter video link here")

    #Search Button
    searchButton = QPushButton()
    searchButton.setText("Find Video")
    searchButton.clicked.connect(searchButton_clicked)

    # Wanted File Type
    audioButton = QRadioButton("Audio only")
    videoButton = QRadioButton("Video only")
    bothButton = QRadioButton("Both combined")
    bothButton.setChecked(True)

    # Video Details
    titleLabel = QLabel("Title: ")
    authorLabel = QLabel("Author: ")
    viewLabel = QLabel("Views: ")
    lengthLabel = QLabel("Length: ")
    thumbLabel = QLabel()

    # Download Location Input
    locBox = QLineEdit()
    locBox.setText("Enter download location here")

    # Download Button
    downButton = QPushButton()
    downButton.setText("Download")
    downButton.clicked.connect(downButton_clicked)

    # Status Indicator
    statusLabel = QLabel("Status: Idle")


    # Layout Design
    layout.addWidget(le, 0, 0, 1, 4)
    layout.addWidget(searchButton, 1, 0, 1, 4)
    layout.addWidget(audioButton, 2, 0)
    layout.addWidget(videoButton, 2, 1)
    layout.addWidget(bothButton, 2, 2)
    layout.addWidget(titleLabel, 4, 2, 1, 2)
    layout.addWidget(authorLabel, 5, 2, 1, 2)
    layout.addWidget(viewLabel, 6, 2, 1, 2)
    layout.addWidget(lengthLabel, 7, 2, 1, 2)
    layout.addWidget(thumbLabel, 4, 0, 4, 2)
    layout.addWidget(locBox, 8, 0, 1, 4)
    layout.addWidget(downButton, 9, 0, 1, 4)
    layout.addWidget(statusLabel, 10, 0, 1, 4)
    win.setLayout(layout)
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    Window()