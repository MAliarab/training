from abc import ABC, abstractmethod


class CompressionStrategy(ABC): # Strategy Abstract

    @abstractmethod
    def compress(self, file: str):
        pass


class ZIPCompression(CompressionStrategy): # Concrete Strategy 1

    def compress(self, file):
        print(f"Compressing file {file} as zip")


class RARCompression(CompressionStrategy): # Concrete Strategy 2

    def compress(self, file):
        print(f"Compressing file {file} as rar")


class FileCompressor: # Context

    def __init__(self, strategy: CompressionStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: CompressionStrategy):
        self._strategy = strategy

    def compress(self, file: str):
        self._strategy.compress(file)


# Client
compressor = FileCompressor(ZIPCompression())
compressor.compress("file.txt")

compressor.set_strategy(RARCompression())
compressor.compress("file.txt")
