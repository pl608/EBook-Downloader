from ebooklib import epub

class MakeBook():
    def __init__(self,title,author=''):
        '''
        Args:
            title: title of the book(str),
            author: author of the book(str)
        '''
        self.title = title
        self.author = author
        self.book = epub.EpubBook()
        self.book.add_author(author)
        self.book.set_title(title)
        self.book.set_identifier('id3786')
        self.chapCount = 0
        self.chaps = []
    def add_chapter(self,content):
        '''
        Args:
            content: data to write as a chapter(str)
        '''
        self.book = epub.EpubBook()
        self.book.set_title(self.title)
        self.book.set_language('en') 
        self.chaps.append(epub.EpubHtml(file_name=f'chap_{self.chapCount}.xhtml',content=content))
        self.chapCount += 1
    
    def add_cover(self,img):
        self.book.set_cover('cover.png', img, create_page=True)
    
    def write_book(self, path):
        '''
        Args:
            path: path to save the book(str)
        '''
        for x in self.chaps:
            self.book.add_item(x)
        epub.write_epub(path,self.book)
