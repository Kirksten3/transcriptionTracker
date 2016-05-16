import threading
import win32com.client as win32
import tkinter as tk
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
        self.initialize_function = {'14.0': self.Word2010,
                                    '15.0': self.Word2013,
                                    '16.0': self.Word2016}.get(self.version, self.Word2010)
        self.doc = self.word.Documents.Add()
        self.word.Visible = True

    @staticmethod
    def Start_Word(details):
        word = Word()
        word.initialize_function(details)

    def Word2010(self, details):
        # take course name, lesson and video name
        doc_start = self.doc.Range(0, 0)
        #this should be replaced with actual course info
        title = details.Course + " - Week " + details.Week + " - " + details.Video + "\n"
        #handle num slides
        title_len = len(title)

        print(title_len)

        doc_start.InsertAfter(title)

        self.doc.Range(self.doc.Paragraphs(1).Range.Start,
                        self.doc.Paragraphs(1).Range.End).Select()

        docText = self.doc.ActiveWindow.Selection
        docText.Style = self.doc.Styles("Title")

        docText.InsertAfter("Slide 1:")

        print(len(self.doc.Content.Text))

        self.doc.Range(title_len, len(self.doc.Content.Text)).Select()
        self.doc.ActiveWindow.Selection.Style = self.doc.Styles("Heading 2")

        sleep(5)

    def Word2013(self, details):
        self.Word2010(details)

    def Word2016(self, details):
        x=5

    def Quit(self):
        self.word.Application.Quit()

    def Quit_No_Save(self):
        self.doc.Close(False)
        self.Quit()

class Word_Details:
    def __init__(self, course_name, week, video_name, num_slides):
        self.Course = str(course_name)
        self.Week = str(week)
        self.Video = str(video_name)
        self.Slides = num_slides

class UI:
    def __init__(self, is_timer=False):
        """
        A generic UI class that will handle the new/open menu,
        the creation menu, and the timer menu for use

        Returns:
            Object, a tkinter object with basic settings initialized
            namely self.Root and self.Mainframe

        """
        self.Root = tk.Tk()
        self.Root.title("Transcription Tracker")
        # on close, hide window
        self.Root.protocol("WM_DELETE_WINDOW", self.Root.iconify)

        # create menu to allow user to exit, use for timer window
        menu_bar = tk.Menu(self.Root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.Destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.Root.config(menu=menu_bar)

        self.Mainframe = ttk.Frame(self.Root, padding="3 3 12 12")
        self.Mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.Mainframe.columnconfigure(0, weight=1)
        self.Mainframe.rowconfigure(0, weight=1)

    def Destroy(self):
        self.Root.destroy()

class Menu(UI):
    # holds the Word_Details class info
    Details = ""

    @staticmethod
    def New_Or_Open():
        ui = UI()
        # button initialization
        ttk.Label(ui.Mainframe, text="Create a new document, or open a current document.")\
            .grid(column=2, row=1, sticky=tk.N)

        ttk.Button(ui.Mainframe, text="New", command= lambda: Menu.Destroy_And_Call(ui, Menu.New_Document))\
            .grid(column=2, row=2, sticky=tk.E)
        ttk.Button(ui.Mainframe, text="Open", command= lambda: Menu.Destroy_And_Call(ui, Menu.Open_Document))\
            .grid(column=3, row=2, sticky=tk.W)

        for child in ui.Mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        ui.Root.mainloop()

    @staticmethod
    def Open_Document():
        x=5

    @staticmethod
    def New_Document():
        ui = UI()

        # variable definitions
        course_name = tk.StringVar()
        week = tk.StringVar()
        video_name = tk.Text(ui.Mainframe, height=3, width=40)
        num_slides = tk.StringVar()

        # creating entries
        course_name_entry = ttk.Entry(ui.Mainframe, width=12, textvariable=course_name)
        week_entry = ttk.Entry(ui.Mainframe, width=3, textvariable=week)
        num_slides_entry = ttk.Entry(ui.Mainframe, width=3, textvariable=num_slides)

        # aligning on grid
        course_name_entry.grid(column=2, row=1, sticky=tk.W)
        week_entry.grid(column=2, row=2, sticky=tk.W)
        video_name.grid(column=2, row=3)
        num_slides_entry.grid(column=2, row=5, sticky=tk.W)

        ttk.Button(ui.Mainframe, text="Go",
                   command=lambda: Menu.Validate_Word_Details(ui,
                                                          Menu.Timer,
                                                          Menu.New_Document,
                                                          Word_Details(course_name.get(),
                                                                       week.get(),
                                                                       video_name.get("1.0", tk.END),
                                                                       num_slides.get())))\
            .grid(column=3, row=6, sticky=tk.E)

        #set up labels for the ui
        ttk.Label(ui.Mainframe, text="Course Name:").grid(column=1, row=1, sticky=tk.W)
        ttk.Label(ui.Mainframe, text="*", foreground="red").grid(column=1, row=1, sticky=tk.E)
        ttk.Label(ui.Mainframe, text="Week Number:").grid(column=1, row=2, sticky=tk.W)
        ttk.Label(ui.Mainframe, text="Video Name:").grid(column=1, row=3, sticky=tk.W)
        ttk.Label(ui.Mainframe, text="*", foreground="red").grid(column=1, row=3, sticky=tk.E)
        ttk.Label(ui.Mainframe, text="Number of Slides:").grid(column=1, row=5, sticky=tk.W)

        ttk.Label(ui.Mainframe, text="Required *", foreground="red").grid(column=1, row=6, sticky=tk.W)

        for child in ui.Mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        course_name_entry.focus()
        # ui.Root.bind('<Return>', main)

        ui.Root.mainloop()


    @staticmethod
    def Timer():
        ui = UI()

        #static "init" function
        Word.Start_Word(Menu.Details)


    @staticmethod
    def Validate_Word_Details(ui, function, calling_function, details):

        # loads word details into static member variable and calls specified function
        Menu.Details = details

        if details.Course == "":
            Menu.Destroy_And_Call(ui, calling_function)
        if details.Video == "":
            Menu.Destroy_And_Call(ui, calling_function)
        if not details.Week.isnumeric() and details.Week != "":
            Menu.Destroy_And_Call(ui, calling_function)
        if not details.Slides.isnumeric() and details.Slides != "":
            Menu.Destroy_And_Call(ui, calling_function)

        Menu.Destroy_And_Call(ui, function)

    @staticmethod
    def Destroy_And_Call(ui, function):
        ui.Destroy()
        function()



# def Start_Word(details):
#     #arg is a Word_Details object
#
#     #new word object
#     word = Word()
#
#     word.initialize_function(details)
#
#     #initialize_document(word.Doc, word.Version)
#
#     #word.quit_no_save()

# def ui():
#     root = Tk()
#     root.title("Transcription Tracker")
#
#     mainframe = ttk.Frame(root, padding="3 3 12 12")
#     mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#     mainframe.columnconfigure(0, weight=1)
#     mainframe.rowconfigure(0, weight=1)
#
#     course_name = StringVar()
#     week = IntVar()
#     video_name = Text(mainframe, height=3, width=40)
#     num_slides = IntVar()
#
#     # text_area = Text()
#     # ScrollBar = Scrollbar(root)
#     # ScrollBar.config(command=text_area.yview)
#     # text_area.config(yscrollcommand=ScrollBar.set)
#     # ScrollBar.pack(side=RIGHT, fill=Y)
#     # text_area.pack(expand=YES, fill=BOTH)
#
#     #creating entry text boxes

#
#
#

if __name__ == '__main__':

    Menu.New_Or_Open()

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