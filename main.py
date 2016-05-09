import threading
import win32com.client as win32
import tkinter
from time import sleep

#
def word():
    """Initialize and open Microsoft Word, with specified title"""
    word = win32.gencache.EnsureDispatch('Word.Application')
    #new document
    doc = word.Documents.Add()
    word.Visible = True
    #sleep(1)

    rng = doc.Range(0,0)
    rng.InsertAfter('Word Application.\n\n')
    #sleep(1)

    rngParagraphs = doc.Range(doc.Paragraphs(1).Range.Start, doc.Paragraphs(1).Range.End)
    rngParagraphs.Select()


    #selection = doc.Sentences(1).Select
    docText = doc.ActiveWindow.Selection

    print(str(docText))

    #closes without saving
    doc.Close(False)
    #quits application
    word.Application.Quit()

if __name__ == '__main__':
    word()


# useful functions
# with a doc defined:
#   doc.Words(num_words).Text : gets the number of words specified by num_words and returns the text
#   doc.Sentences(num_sentences).Text : returns sentences specified
#   doc.Select() : selects the area specified by a range
#   doc.ActiveWindow.Selection : assigns the selection to a variable
#   doc.Range(start, end): specifies a range to get, which can be added to or edited or removed