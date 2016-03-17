__author__ = 'mhbashari'

import pandas as pd


class ExcelReader:
    def __init__(self, excel_address="NRC-Emotion-Lexicon-v0.92-InManyLanguages-web.xlsx"):
        self.excel_address = excel_address
        self.data = {}

    def load(self):
        xl = pd.ExcelFile("dummydata.xlsx")

    def get_translation(self, word):
        return self.data[word]
