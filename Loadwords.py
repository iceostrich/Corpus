__author__ = 'liujian'
from xml.etree.ElementTree import parse
from PyQt5 import QtWidgets
from UI import Ui_Form
import sys


print('Test!')

doc = parse('0001-0500.xml')
'''
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print(title)
    print(date)
    print(link)
    print()

'''

class MyWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.getword)

    def getword(self):
        for item in doc.iterfind('item'):
            word = 'Word:' + item.findtext('word')
            trans = 'Trans:' + item.findtext('trans')
            phonetic = 'Phonetic:' + item.findtext('phonetic')
            tags = 'Tags:' + item.findtext('tags')
            progress = 'Progress:' + item.findtext('progress')
            self.textBrowser.append(word)
            self.textBrowser.append(trans)
            self.textBrowser.append(phonetic)
            self.textBrowser.append(tags)
            self.textBrowser.append(progress)
            self.textBrowser.append('='*20)

app = QtWidgets.QApplication(sys.argv)
MyShow = MyWindow()
MyShow.show()
sys.exit(app.exec_())