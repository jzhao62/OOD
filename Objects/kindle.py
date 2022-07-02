from enum import Enum
from abc import ABC, abstractmethod


class Format(Enum):
    EPUB = 'epub'
    PDF = 'pdf'
    MOBI = 'mobi'

    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content


class book:

    def __init__(self, format):
        self.format = format

    def get_format(self):
        return self.format


class EbookReaderFactory:
    def create_reader(self, book):

        curr_format = book.get_format()

        if curr_format == Format.EPUB:
            return EpubReader(book)
        if curr_format == Format.PDF:
            return PdfReader(book)

        return None


class EbookReader(ABC):
    def __init__(self, book):
        self.book = book

    @abstractmethod
    def read_book(self): pass

    @abstractmethod
    def display_reader_type(self): pass


class EpubReader(EbookReader):
    def __init__(self, book):
        super().__init__(book)

    def read_book(self):
        return self.book.get_format().get_content()

    def display_reader_type(self):
        return 'USING EPUB READER'


class PdfReader(EbookReader):

    def __init__(self, book):
        super().__init__(book)

    def read_book(self):
        return self.book.get_format().get_content()

    def display_reader_type(self):
        return 'USING PDF READER'


class Kindle:
    def __init__(self):
        self.books = []
        self.reader_factory = EbookReaderFactory()

    def read_book(self, book):
        reader = self.reader_factory.create_reader(book)
        if reader is None:
            raise "Cannot read this format"

        return reader.display_reader_type() + ' , book content is: ' + reader.read_book()


kindle = Kindle()
print(kindle.read_book(book(Format.EPUB)))
