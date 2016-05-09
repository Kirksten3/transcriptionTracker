import threading
import win32com.client as win32
import tkinter
from time import sleep

class Word:
    def __init__(self):
        self.Word = win32.gencache.EnsureDispatch('Word.Application')
        self.Version = self.Word.Version
        self.Doc = self.Word.Documents.Add()
        #make visible
        self.Word.Visible = True
    def Quit(self):
        self.Word.Application.Quit()
    def QuitNoSave(self):
        self.Doc.Close(False)
        self.Quit()

class Selection:
    """Must be a Word Selection Object in self.Selection"""
    def __init__(self, selectionObject):
        self.Selection = selectionObject
    def ChangeFont(self, font=False, fontSize, fontStyle):
        self.Selection.Font.Name = font


def initialize_document(doc, version):
    """Initialize and open Microsoft Word, with specified title"""



    #sleep(1)

    rng = doc.Range(0,0)
    rng.InsertAfter('Word Application.\n\n')
    #sleep(1)

    print(len(doc.Content.Text))

    rngParagraphs = doc.Range(doc.Paragraphs(1).Range.Start, doc.Paragraphs(1).Range.End)
    rngParagraphs.Select()
    rngParagraphs.Font.Name = "Arial"
    #doc.ActiveWindow.Selection.Font.Size(14)

    #selection = doc.Sentences(1).Select
    docText = doc.ActiveWindow.Selection
    docText.Font.Size = 20

    print(str(docText))
    sleep(5)
    #closes without saving
    doc.Close(False)


def main():
    #new word object
    word = Word()

    initialize_document(word.Doc, word.Version)

    word.QuitNoSave()

if __name__ == '__main__':
    main()


# useful functions or members
# with word defined:
#   word.Version : the current word version used
#   word.Visible = bool : bool determines if word is visible or not, required
#
# with a doc defined:
#   doc.Words(num_words).Text : gets the number of words specified by num_words and returns the text
#   doc.Sentences(num_sentences).Text : returns sentences specified
#   doc.Select() : selects the area specified by a range
#   doc.ActiveWindow.Selection : assigns the selection to a variable
#   doc.Content.Text : returns all text in the document. USE THIS TO CHECK IF IT HAS BEEN ADDED TO
#   doc.Range(start, end): specifies a range to get, which can be added to or edited or removed
#
# with a selection or a range:
#   selection.Font.Size = value : where selection is the selection, and size is assignable
#   selection.Font.Name = name : where name is a font name, i.e. "Arial"
#   selection.Font.Bold = bool : where bool is True or False