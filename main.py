from PyQt5.QtWidgets import QApplication

import json
import sys

import DownloadStation
import LoginDialog


class main():
    def __init__(self):
        try:
            with open('accounts.json', 'rt', encoding='UTF8') as json_file:
                global synoURL, synoID, synoPW

                jsonData = json.load(json_file)
                self.synoURL = jsonData["Server"]
                self.synoID = jsonData["ID"]
                self.synoPW = jsonData["PW"]

            self.openDownloadStation()
        except FileNotFoundError:
            self.openLogin()

    def openDownloadStation(self):
        self.window = DownloadStation.DownloadStation(self.synoURL, self.synoID, self.synoPW)

    def openLogin(self):
        self.window = LoginDialog.LoginDialog()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    execute = main()
    sys.exit(app.exec_())
