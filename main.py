import json
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter.ttk import Style
from variables import *

class App(object):

    def __init__(self):

        filetypes = (
            ('JSON file', '*.json'),
        )

        def browse_button():
            folder_path = StringVar()
            filename = filedialog.askopenfile(
                title="Open a .json file",
                filetypes = filetypes,
                initialdir='/'
            )
            folder_path.set(filename)
            if filename != "":
                showinfo(
                    title='Selected file',
                    message=filename.name
                )
                dragAndDropSection.destroy()
                textArea = Text(functionalFrame, height=12)
                textArea.pack()
                JSONfile = open(filename.name,"r")
                data = json.loads(JSONfile.read())
                for i in data:
                     textArea.insert('1.0',i)
                JSONfile.close()

        # basic application window settings
        self.window = Tk()
        self.window.geometry('{}x{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.window.minsize(MIN_WINDOW_WIDTH, WINDOW_HEIGHT)
        self.window.title(WINDOW_TITLE)
        self.window.resizable(X_RESIZE_WINDOW, Y_RESIZE_WINDOW)
        self.window.iconbitmap(ICON)
        style = Style(self.window)
        style.theme_use('clam')

        # build main sections, upper section is a digital section aka view section for all information, bottom section is our functional section for all interactive activities
        digitalFrame = Frame(self.window,
                             bg=DIGITAL_FRAME_BACKGROUND)
        digitalFrame.place(relheight=RELHEIGHT_DIGITAL_FRAME,
                           relwidth=1)
        digitalFrame.config()
        functionalFrame = Frame(self.window, bg=FUNCTIONAL_FRAME_BACKGROUND)
        functionalFrame.place(rely=RELHEIGHT_DIGITAL_FRAME,
                              relheight=RELHEIGHT_FUNCTIONAL_FRAME,
                              relwidth=1)
        functionalFrame.config()

        #Button for searching JSON file with QMK information
        dragAndDropSection = Button(functionalFrame,
                                    text = TEXT_SEARCH_BUTTON,
                                    bg = BACKGROUND_SEARCH_BUTTON,
                                    activebackground = ACTIVEBACKGROUND_SEARCH_BUTTON,
                                    fg = FOREGROUND_SEARCH_BUTTON,
                                    height = HEIGHT_SEARCH_BUTTON,
                                    width = WIDTH_SEARCH_BUTTON,
                                    command=browse_button)
        dragAndDropSection.pack(pady=PADY_SEARCH_BUTTON)
        dragAndDropSection.config()
        self.window.mainloop()


def main():
    app = App()


main()
