from abc import ABC, abstractmethod


# Component interface
class FileSystemComponent(ABC):

    @abstractmethod
    def show(self, indent=0):
        pass


# Leaf
class File(FileSystemComponent):

    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print(" " * indent + f"File -> {self.name}")


# Composite class
class Folder(FileSystemComponent):

    def __init__(self, name):
        self.name = name
        self._children = []

    def add(self, child: FileSystemComponent):
        self._children.append(child)

    def remove(self, child):
        self._children.remove(child)

    def show(self, indent=0):
        print(" " * indent + f"Folder -> {self.name}:")
        for child in self._children:
            child.show(indent + 2)


def client():
    file1 = File("file1.txt")
    file2 = File("file2.sh")
    file3 = File("file3.docx")
    file4 = File("file4.pdf")

    folder1 = Folder("docs")
    folder2 = Folder("scripts")

    folder1.add(file3)
    folder1.add(file4)

    folder2.add(file2)

    root_folder = Folder("root")

    root_folder.add(file1)
    root_folder.add(folder1)
    root_folder.add(folder2)

    root_folder.show()


client()
