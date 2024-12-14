import csv
import os.path
import requests
import re
from PyQt6.QtWidgets import *
from gui import *
import datetime


class Logic(QMainWindow, Ui_mainWindow):
    """
    A class for the GUI logic
    """
    FIELDNAMES = ['searchCat', 'gcItemNumber', 'brand', 'displayName', 'condition', 'seoUrl', 'listPrice', 'price',
                  'storeName', 'firstDate', 'priceHistory']

    def __init__(self) -> None:
        """
        Method that sets the default values for Logic class
        """
        super().__init__()
        self.setupUi(self)
        self.items_TableWidget.setColumnWidth(0, 10)
        self.items_TableWidget.setColumnWidth(1, 100)
        self.items_TableWidget.setColumnWidth(2, 700)
        self.items_TableWidget.setColumnWidth(3, 100)
        self.items_TableWidget.setColumnWidth(4, 100)

        self.search_pushButton.clicked.connect(lambda: self.get_html_file())
        self.exit_pushButton.clicked.connect(self.close)

    def get_html(self) -> None:
        """
        Method that could be used to get HTML data from a URL - not used in this example
        """
        #'https://www.guitarcenter.com/Used/Ibanez/Guitars.gc?Ntt=prestige&Ns=pLH&recsPerPage=96'

        htmldata = requests.get(self.searchUrl_Entry.text())
        if htmldata.status_code == 200:
            with open('GSpage2.html', 'w') as file:
                file.write(htmldata.text)

    def get_html_file(self) -> None:
        """
        Method to take submitted html file, process it, and display it
        """
        if self.searchName_Entry.text() == '':
            self.outputText_Label.setText("Enter a Search Name")
        else:
            search_name = self.searchName_Entry.text()
            if os.path.exists(self.searchUrl_Entry.text()):
                with open(self.searchUrl_Entry.text(), 'r') as file:
                    htmldata = file.read()
                self.parse_html(htmldata, search_name)
                self.display_data()
            else:
                self.outputText_Label.setText("Invalid html file location")

    def display_data(self) -> None:
        """
        Method that displays the data from temp_data.csv to items_TableWidget
        """
        with open('temp_data.csv', 'r') as file:
            reader = csv.DictReader(file)

            row = 0
            for guitar in reader:
                self.items_TableWidget.setRowCount(row + 1)
                if guitar['price']:
                    self.items_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(f"$ {guitar['price']}"))
                else:
                    self.items_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(f"$ {guitar['listPrice']}"))
                self.items_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(guitar['displayName']))
                self.items_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(guitar['firstDate']))
                self.items_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(f"$ {guitar['listPrice']}"))
                row += 1

    def parse_html(self, htmldata:str, search_name:str) -> None:
        """
        Method that processes the html data and writes it to temp_data.csv. FIELDNAMES are the fieldnames for the csv file.
            FIELDNAMES = ['searchCat', 'gcItemNumber', 'brand', 'displayName', 'condition', 'seoUrl', 'listPrice', 'price',
                  'storeName', 'firstDate', 'priceHistory']
        :param htmldata: string input from the user submitted html file
        :param search_name: string input from the user

        """
        tempDict = dict.fromkeys(self.FIELDNAMES, '')
        time = datetime.datetime.now()
        form_time = time.strftime("%Y-%m-%d, %H:%M")

        with open('temp_data.csv', 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.FIELDNAMES)
            csv_writer.writeheader()
            #csv_writer.writerow({'searchCat': f'**{search_name}'})
            search_results = re.search('"hits":(.*?),"hitsPerPage"', htmldata)      #strips the search hits out of the html file

            if search_results:
                results = search_results.group().split("},{")                              #splits the entries into a list

                for result in results:
                    for field in self.FIELDNAMES:                                          #the fieldnames are not in any particular order
                        if field == 'condition':                                            #Regular expressions are used to strip out the value.
                            tempSearch = re.search(r'u003e .+?"', result)
                        elif field == 'price' or field == 'listPrice':
                            tempSearch = re.search(field + '":.+?[,}]', result)
                        else:
                            tempSearch = re.search(field + '":".+?"', result)

                        if tempSearch:                                                      #Removing the fieldname and other unwanted characters
                            if field == 'brand':
                                tempDict[field] = tempSearch.group().lstrip(field + r'":"{"value":"').rstrip('",}')
                            elif field == 'condition':
                                tempDict[field] = tempSearch.group().lstrip(r'\u003e ').rstrip('",')
                            else:
                                tempDict[field] = tempSearch.group().lstrip(f'{field}+":"').rstrip('",}')

                    if field == 'listPrice' and tempDict['price'] == '': tempDict['price'] = tempDict['listPrice']
                    tempDict['priceHistory'] = f"{form_time}, {tempDict['price']}"          #adding date, time, and search category
                    tempDict['firstDate'] = form_time
                    tempDict['searchCat'] = search_name
                    csv_writer.writerow(tempDict)
                    tempDict = dict.fromkeys(self.FIELDNAMES, '')

            else:
                self.outputText_Label.setText("No Results")
        csv_file.close()