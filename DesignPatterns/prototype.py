from abc import ABC, abstractmethod
from copy import deepcopy


class DocPrototype(ABC):

    @abstractmethod
    def clone(self):
        pass


class Invoice(DocPrototype):

    def __init__(self, amount: int, code: str):
        self.amount = amount
        self.code = code

    def get(self):
        print(f"Invoice {self.code} with amount {self.amount}")
        print("-" * 10)

    def clone(self) -> "Invoice":
        return deepcopy(self)


class Report(DocPrototype):

    def __init__(self, title: str, author: str, content: str):
        self.title = title
        self.author = author
        self.content = content

    def get(self):
        print(f"Report {self.title} by {self.author}\nContent: {self.content}")
        print("-" * 10)

    def clone(self) -> "Report":
        return deepcopy(self)


# Use prototype

# Create original invoice
invoice = Invoice(2300, "INV-123")

# Clone invoice
cloned_invoice = invoice.clone()
cloned_invoice.code = "INV-124"

# Create original report
report = Report("Marketing", "Haji", "%20 increasing sale from last month")

# Clone report
cloned_report = report.clone()
cloned_report.title = "Financial"
cloned_report.author = "Dadash"

# Results
invoice.get()
cloned_invoice.get()

report.get()
cloned_report.get()
