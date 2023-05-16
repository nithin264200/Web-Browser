from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('http://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        #navigationbar

        navbar=QToolBar()
        self.addToolBar(navbar)
        back_button=QAction('<',self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        forward_button=QAction('>',self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        refresh_button=QAction('refresh',self)
        refresh_button.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_button)

        home_button=QAction('Home',self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)

        youtube_button=QAction('DINESH',self)
        youtube_button.triggered.connect(self.navigate_youtube)
        navbar.addAction(youtube_button)

        gmail_button=QAction('gmail',self)
        gmail_button.triggered.connect(self.navigate_gmail)
        navbar.addAction(gmail_button)

        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def navigate_gmail(self):
        self.browser.setUrl(QUrl('http://gmail.com'))

    def navigate_youtube(self):
        self.browser.setUrl(QUrl('http://youtube.com'))

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def update_url(self, v):
        self.url_bar.setText(v.toString())

app=QApplication(sys.argv)
QApplication.setApplicationName('MyBrowser')
window=Mainwindow()
app.exec_()





