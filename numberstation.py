import os
import sys
import datetime
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox
from PyQt5.QtWidgets import QPlainTextEdit, QFileDialog, QMainWindow, QGridLayout
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QLabel, QMessageBox
from PyQt5.QtCore import pyqtSlot
from pydub import AudioSegment

station = 'E06'
message_text = ''
output_filename = ''

class App(QWidget):

	def __init__(self):
		super().__init__()
		self.title = 'Numbers Station Message Synthesizer'
		self.setFixedSize(600,400)
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.center()

		self.inputbox = QPlainTextEdit(self)
		self.inputbox.move(10, 10)
		self.inputbox.resize(580, 340)

		self.combo = QComboBox(self)
		self.combo.addItem('E06')
		self.combo.addItem('E07')
		self.combo.move(10, 361)
		self.combo.resize(45, 21)
		self.combo.activated[str].connect(self.onActivated)
		
		self.browsebtn = QPushButton('Browse...', self)
		self.browsebtn.setToolTip('Choose where you want your audio file to save')
		self.browsebtn.move(60, 360)
		self.browsebtn.clicked.connect(self.browse_on_click)

		self.startbtn = QPushButton('Start', self)
		self.startbtn.setToolTip('Starts the conversion of your typed message into audio')
		self.startbtn.move(140, 360)
		self.startbtn.clicked.connect(self.start_on_click)

		self.status = QLabel(self)
		self.status.move(500, 365)
		self.status.setText('Ready.    ')

		self.show()

	def center(self):
		qtRectangle = self.frameGeometry()
		centerPoint = QDesktopWidget().availableGeometry().center()
		qtRectangle.moveCenter(centerPoint)
		self.move(qtRectangle.topLeft())

	def onActivated(self, text):
		global station
		station = str(text)

	def browse_on_click(self):
		name = QFileDialog.getSaveFileName(self, 'Save', '.mp3')
		global output_filename
		output_filename = name[0]
		self.status.setText('Ready.    ')


	def start_on_click(self):
		global message_text
		global output_filename
		message_text = self.inputbox.toPlainText()
		if message_text == '':
			QMessageBox.warning(self, 'Warning', 'Empty message box. Please input a message.', QMessageBox.Ok)
			return
		if output_filename == '':
			QMessageBox.warning(self, 'Warning', 'No file destination selected.\nPlease indicate where you want the file to be saved.', QMessageBox.Ok)
			return
		self.status.setText('Working...')
		message = list(message_text)
		message = listsetup(message, station)
		parser(message)
		self.status.setText('Complete. ')


def listsetup(list, station):
	filename_list = []
	for val in list:
		filename = str(os.getcwd()) + '/' + str(station) + '/' + str(val) + '.mp3'
		filename_list.append(filename)
	return filename_list

def parser(list):
	message = []
	for val in list:
		addition = AudioSegment.from_mp3(val)
		message.append(addition)
	output = sum(message)
	global output_filename
	output.export(output_filename, format = "mp3")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())