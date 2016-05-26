import win32com.client as win32
import tkinter as tk
from tkinter import ttk
from time import sleep
from enum import Enum
import requests

# file://oande.sig.oregonstate.edu/Ecampus/Files/CDT%20Student%20Workers/Jake/Projects/Transcription%20Tracker/HTML%20CSS/index.html

# Have a menu that allows users to pick whether to start a new transcript or open an existing one
# On new have them enter: course name, video name, and lesson
# On open just have a selection window


class DOC_STATUS(Enum):
    DOC_LENGTH_CHANGED = 0
    DOC_LENGTH_SAME = 1
    DOC_CLOSED = 2


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
        # this should be replaced with actual course info

        title = details.Course + " - Week " + details.Week + " - " + details.Video + "\n"

        if details.Week == "":
            title = details.Course + " - " + details.Video + "\n"

        #handle num slides
        title_len = len(title)

        print(title_len)

        doc_start.InsertAfter(title)

        self.doc.Range(self.doc.Paragraphs(1).Range.Start,
                        self.doc.Paragraphs(1).Range.End).Select()

        docText = self.doc.ActiveWindow.Selection
        docText.Style = self.doc.Styles("Title")

        docText.InsertAfter("Slide 1:")

        if details.Slides != "" and details.Slides != 0:
            for i in range(2, int(details.Slides)):
                location = self.doc.Range(0, len(self.doc.Content.Text))
                location.InsertAfter("Slide " + str(i) + ":\n")

        print(len(self.doc.Content.Text))

        self.doc.Range(title_len, len(self.doc.Content.Text)).Select()
        self.doc.ActiveWindow.Selection.Style = self.doc.Styles("Heading 2")

    def Word2013(self, details):
        self.Word2010(details)

    def Word2016(self, details):
        self.Word2010(details)

    @staticmethod
    def Check_Word_Status():
        """
        Check and see if word is still running, if not then save timer number and update
        """
        try:
            win32.GetActiveObject('Word.Application')
        except:
            return False
        else:
            # instance exists!
            return True

    @staticmethod
    def Check_Document_Length(previous_length):
        if not Word.Check_Word_Status():
            return DOC_STATUS.DOC_CLOSED

        else:
            word = win32.GetActiveObject('Word.Application')
            doc = word.ActiveDocument
            if len(doc.Content.Text) == previous_length:
                return DOC_STATUS.DOC_LENGTH_SAME, previous_length
            else:
                return DOC_STATUS.DOC_LENGTH_CHANGED, len(doc.Content.Text)

    @staticmethod
    def Get_Document_Length():
        if not Word.Check_Word_Status():
            return DOC_STATUS.DOC_CLOSED

        else:
            word = win32.GetActiveObject('Word.Application')
            doc = word.ActiveDocument
            return len(doc.Content.Text)

    def Quit(self):
        self.word.Application.Quit()

    def Quit_No_Save(self):
        self.doc.Close(False)
        self.Quit()


class WordDetails:
    def __init__(self, course_name, week, video_name, num_slides):
        self.Course = str(course_name)
        self.Week = str(week)
        self.Video = str(video_name)
        self.Slides = str(num_slides)


class UI:
    def __init__(self):
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


class User():

    def __init__(self):
        # error here
        self.LoginPath = 'https://dev.ecampus.oregonstate.edu/transcriptionTracker/login.php'
        self.ui = UI()
        # error label so each handler can modify it
        self.ErrorLabel = ttk.Label(self.ui.Mainframe, text="", foreground='red')
        self.Name = ""
        self.Id = ""
        self.Login()

    def Login(self):
        ttk.Label(self.ui.Mainframe, text="Login or Register. If logging in, only an ONID Username is necessary.") \
            .grid(column=1, row=1, sticky=tk.W)
        ttk.Label(self.ui.Mainframe, text="ONID Username:").grid(column=1, row=3, sticky=tk.W)
        ttk.Label(self.ui.Mainframe, text="Name:").grid(column=1, row=4, sticky=tk.W)

        # define error label so that login / register can update if an error occurs
        self.ErrorLabel.grid(column=1,row=2, sticky=tk.W)

        osu_id = tk.StringVar()
        name = tk.StringVar()

        # set up entries with placeholders, will need an event handler for focus in
        tk.Entry(self.ui.Mainframe, width=15, textvariable=osu_id).grid(column=1, row=3)
        tk.Entry(self.ui.Mainframe, width=15, textvariable=name).grid(column=1, row=4)

        ttk.Button(self.ui.Mainframe, text="Login",
                   command=lambda: self.Handle_Login(osu_id.get())).grid(column=2, row=5, sticky=tk.E)

        ttk.Button(self.ui.Mainframe, text="Register",
                   command=lambda: self.Handle_Register(osu_id.get(), name.get())).grid(column=3, row=5, sticky=tk.E)

        for child in self.ui.Mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        self.ui.Root.mainloop()

    def Handle_Login(self, id):
        if not User.Validate_User_Credentials(id, 0, 'Login'):
            self.ErrorLabel.config(text='Invalid Credentials Entered')
            return False

        else:
            response = requests.post(self.LoginPath,
                                     data = {'id': id})
            userResult = User.Validate_Server_Response(response)
            if not userResult:
                self.ErrorLabel.config(text='Error attempting to Login')
                return False

            else:
                self.Name = userResult
                self.Id = id

            self.Valid = True
            self.ui.Destroy()
            return True

    def Handle_Register(self, id, name):
        if not User.Validate_User_Credentials(id, name, 'Register'):
            self.ErrorLabel.config(text='Invalid Credentials Entered')
            return False

        else:
            response = requests.post(self.LoginPath,
                                     data = {'name': name, 'id': id})
            userResult = User.Validate_Server_Response(response)
            if not userResult:
                self.ErrorLabel.config(text='Error attempting to Register')
                return False
            else:
                self.Name = userResult
                self.Id = id
            self.Valid = True
            self.ui.Destroy()
            return True

    @staticmethod
    def Validate_User_Credentials(id, name, callingFunc):
        if callingFunc == 'Register' and (name == "" or id == ""): return False
        elif callingFunc == 'Login' and id == "": return False
        return True

    @staticmethod
    def Validate_Server_Response(text):
        data = text.json()
        print(data)
        if not data['success']:
            return False
        else:
            return data['name']


class Menu(UI):
    # holds the Word_Details class info
    Details = ""

    @staticmethod
    def New_Or_Open(name):
        ui = UI()

        ttk.Label(ui.Mainframe, text="Login Successful, Welcome " + name + ".", foreground="green")\
            .grid(column=1,row=1, sticky=tk.W)

        # button initialization
        ttk.Label(ui.Mainframe, text="Create a new document, or open a current document.")\
            .grid(column=1, row=2, sticky=tk.N)

        ttk.Button(ui.Mainframe, text="New", command= lambda: Menu.Destroy_And_Call(ui, Menu.New_Document))\
            .grid(column=2, row=3, sticky=tk.E)
        ttk.Button(ui.Mainframe, text="Open", command= lambda: Menu.Destroy_And_Call(ui, Menu.Open_Document))\
            .grid(column=3, row=3, sticky=tk.W)

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
                                                          WordDetails(course_name.get(),
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

        #init empty timer
        timer_field = ['0', '0', ':', '0', '0', ':', '0', '0']


        ui = UI()

        #static "init" function
        Word.Start_Word(Menu.Details)
        previous_doc_length = Word.Get_Document_Length()
        print(previous_doc_length)
        ttk.Label(ui.Mainframe, text="Time Transcribing: ").grid(column=1, row=1, sticky=tk.W)
        time_label = ttk.Label(ui.Mainframe, text=Menu.Print_Time(timer_field))
        time_label.grid(column=2, row=1)
        ttk.Button(ui.Mainframe, text="Save and Quit", command=lambda x: x*5).grid(column=2, row=2, sticky=tk.E)

        for child in ui.Mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        Menu.Timer_Update(ui, timer_field, time_label, previous_doc_length, 0)
        ui.Root.mainloop()

    @staticmethod
    def Print_Time(timer):
        return ''.join(timer)

    @staticmethod
    def Timer_Update(ui, timer, label, previous_length, count=0):

        # timer layout: ['0', '0', ':', '0', '0', ':', '0', '0']

        seconds = int(timer[6] + timer[7])
        minutes = int(timer[3] + timer[4])
        hours = int(timer[0] + timer[1])

        if seconds == 59:
            if minutes == 59:
                seconds = 0
                minutes = 0
                hours += 1
            else:
                seconds = 0
                minutes += 1
        else:
            seconds += 1

        print(count)

        # every 180 seconds check to see if document length has changed
        # if it hasn't remove the last three minutes or if document has closed
        if count % 180 == 0:
            print(count)
            status, new_length = Word.Check_Document_Length(previous_length)
            if status == DOC_STATUS.DOC_LENGTH_SAME:
                minutes = minutes - 3
            elif status == DOC_STATUS.DOC_LENGTH_CHANGED:
                previous_length = new_length
            elif status == DOC_STATUS.DOC_CLOSED:
                # CLOSE DOCUMENT HERE
                exit(1)

        string_seconds = str(seconds)
        string_minutes = str(minutes)
        string_hours = str(hours)

        # had to declare new array because strings had problems...
        temp_time = []
        if len(string_hours) == 1:
            string_hours = '0' + string_hours

        temp_time.append(string_hours[0])
        temp_time.append(string_hours[1])
        temp_time.append(':')

        if len(string_minutes) == 1:
            string_minutes = '0' + string_minutes

        temp_time.append(string_minutes[0])
        temp_time.append(string_minutes[1])
        temp_time.append(':')

        if len(string_seconds) == 1:
            string_seconds = '0' + string_seconds

        temp_time.append(string_seconds[0])
        temp_time.append(string_seconds[1])


        count += 1
        # update label
        label.configure(text=Menu.Print_Time(temp_time))
        ui.Root.after(1000, lambda: Menu.Timer_Update(ui, temp_time, label, previous_length, count))

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

if __name__ == '__main__':
    # validate user
    user = User()

    # menu to start, pass in user's name
    Menu.New_Or_Open(user.Name)


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