import threading
import win32com.client as win32
from tkinter import *
from tkinter import ttk
from time import sleep

# file://oande.sig.oregonstate.edu/Ecampus/Files/CDT%20Student%20Workers/Jake/Projects/Transcription%20Tracker/HTML%20CSS/index.html

# Have a menu that allows users to pick whether to start a new transcript or open an existing one
# On new have them enter: course name, video name, and lesson
# On open just have a selection window

class Word:
    def __init__(self):
        """
        Word.__init__:
            This initialization creates a Word object which contains
            details about the document and Microsoft Word. Including
            the version, the document, and the Word context from
            pyWin32

        Returns:
            A Word Object containing, word context, word version,
            and the document.
        """
        self.word = win32.gencache.EnsureDispatch('Word.Application')
        self.version = self.word.Version
        self.initialize_function = {'14.0': self.word2010,
                                    '15.0': self.word2013}.get(self.version, self.word2010)
        self.doc = self.word.Documents.Add()
        self.word.Visible = True

    def word2010(self):
        # take course name, lesson and video name
        rng = self.doc.Range(0, 0)
        #this should be replaced with actual course info
        title = "ST 351 – Lesson 3.1 – Stratified Sample Example\n"
        title_len = len(title)
        print(title_len)
        rng.InsertAfter(title)

        self.doc.Range(self.doc.Paragraphs(1).Range.Start,
                        self.doc.Paragraphs(1).Range.End).Select()

        docText = self.doc.ActiveWindow.Selection
        docText.Style = self.doc.Styles("Title")

        docText.InsertAfter("Slide 1:")

        print(len(self.doc.Content.Text))

        self.doc.Range(title_len, len(self.doc.Content.Text)).Select()
        self.doc.ActiveWindow.Selection.Style = self.doc.Styles("Heading 2")

        sleep(5)

    def word2013(self):
        x=5

    def quit(self):
        self.word.Application.Quit()

    def quit_no_save(self):
        self.doc.Close(False)
        self.quit()

class Selection:
    def __init__(self, selection_object):
        """
        Selection.__init__:
            This creates a Selection object, which is simply a wrapper for
            the VBA word selection object.

        Args:
            selectionObject (VBA Selection Object): This should be a range of
                text that has been selected in the word document. Text is
                selected through use of the .Select() function

        Returns: A Wrapped Selection Object
        """

        self.Selection = selection_object

    def change_font(self, font="", font_size=None, font_style=(False, False)):
        """
        change_font:
            This function modifies a selection object that has been
            set on initialization, with the following arguments

        Args:
            font (string): A font to select, e.g. 'Times New Roman'
            font_size (int): A size to make the font
            font_style (bool tuple): Specifies whether to use bold and italics
                e.g. (True, False): use bold not italics

        Returns:
            void: Simply modifies the text in the selection of the word document
        """
        if font is not "":
            self.Selection.Font.Name = font
        if font_size is not None:
            self.Selection.Font.Size = font_size
        self.Selection.Font.Bold = font_style[0]
        self.Selection.Font.Italics = font_style[1]

    def set_title_style(self):
        self.Selection.Font.StylisticSet = 8

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

    word.initialize_function()

    #initialize_document(word.Doc, word.Version)

    word.quit_no_save()

def ui():
    root = Tk()
    root.title("Transcription Tracker")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    course_name = StringVar()
    week = StringVar()
    video_name = StringVar()
    num_slides = IntVar()

    #creating entry text boxes
    course_name_entry = ttk.Entry(mainframe, width=5, textvariable=course_name)
    week_entry = ttk.Entry(mainframe, width=3, textvariable=week)
    video_name_entry = ttk.Entry(mainframe, width=12, textvariable=video_name)
    num_slides_entry = ttk.Entry(mainframe, width=3, textvariable=num_slides)

    #aligning on grid
    course_name_entry.grid(column=1, row=1, sticky=(N, W))
    week_entry.grid(column=2, row=1, sticky=(N))
    video_name_entry.grid(column=1, row=2, sticky=(N, W))
    num_slides_entry.grid(column=3, row=1, sticky=(N, E))


    ttk.Button(mainframe, text="Go", command=main).grid(column=3, row=3, sticky=E)

    #set up labels for the ui

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    course_name_entry.focus()
    root.bind('<Return>', main)

    root.mainloop()

if __name__ == '__main__':
    ui()

# VBA -> Python notes:
#   ActiveDocument refers to doc in the Word class
#
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
#   doc.Range(start, end) : specifies a range to get, which can be added to or edited or removed
#   doc.Styles(style_name) : when assigned to a selection's .Style property it will change it depending
#                            on what style_name is, used as "Title" in this program
#
# with a selection or a range:
#   selection.Font.Size = value : where selection is the selection, and size is assignable
#   selection.Font.Name = name : where name is a font name, i.e. "Arial"
#   selection.Font.Bold = bool : where bool is True or False