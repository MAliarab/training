from abc import ABC, abstractmethod


class DataParser(ABC):

    def parse_data(self, file: str):
        self.read_data(file)
        self.validate()
        self.tokenize()
        self.remove_stop_words()

    @abstractmethod
    def read_data(self, file: str):
        pass

    def validate(self):
        print(f"Validating data ...")

    def tokenize(self):
        print(f"Tokenizing ...")

    def remove_stop_words(self):
        print(f"Removing stop words ...")


class ExcelDataParser(DataParser):

    def read_data(self, file):
        print(f"Reading data from excel file: {file}")


class WordDataParser(DataParser):

    def read_data(self, file):
        print(f"Reading data from word file: {file}")


# Client
print("-------- Parsing word file ---------")
word_parser = WordDataParser()
word_parser.parse_data("file.docx")

print("-------- Parsing excel file ---------")
excel_parser = ExcelDataParser()
excel_parser.parse_data("file.xlsx")
