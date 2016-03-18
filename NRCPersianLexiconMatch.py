__author__ = 'mhbashari'

import xlrd as xrd


class ExcelReader:
    def __init__(self, excel_address="NRC-Emotion-Lexicon-v0.92-InManyLanguages-web.xlsx"):
        self.excel_address = excel_address
        self.data = {}

    def load(self, col_idx=22):  # default for persian (in current version)
        xl_workbook = xrd.open_workbook(self.excel_address)
        sheet_names = xl_workbook.sheet_names()
        xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
        for row_idx in range(1, xl_sheet.nrows):
            translation = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
            english = xl_sheet.cell(row_idx, 0)  # Get cell object by row, col
            if translation.value is not None and len(translation.value) > 0:
                self.data[english.value] = translation.value

    def get_translation(self, word):
        return self.data[word]

    def has_key(self, key):
        return key in self.data.keys()


if __name__ == "__main__":
    reader = ExcelReader()
    reader.load()
    engligh_text_file = open("NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt", "r", encoding="utf-8")
    destionation_text_file = open("NRC-emotion-lexicon-wordlevel-persian-v0.92.txt", "w", encoding="utf-8")
    for line in engligh_text_file.readlines():
        spl = line.split("\t")
        word, emotion, value = spl[0], spl[1], spl[2]
        if reader.has_key(word):
            destionation_text_file.write("\t".join([reader.get_translation(word), emotion, value]))
