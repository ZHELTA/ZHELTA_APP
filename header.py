from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter.ttk import Style
from turtle import width
from variables import *


class Header(object):
    def __init__(self, windowVariable):
        headerFrame = Frame(windowVariable,
                            bg=HEADER_FRAME_BACKGROUND)
        headerFrame.place(relheight=RELHEIGHT_HEADER_FRAME,
                          relwidth=1.0)
        # Header Buttons
        keyMapButton = Button(headerFrame,
                              text="KeyMap",
                              height=100,
                              width=20,
                              bg=BACKGROUND_SEARCH_BUTTON,
                              activebackground=ACTIVEBACKGROUND_SEARCH_BUTTON,
                              activeforeground=FOREGROUND_SEARCH_BUTTON,
                              fg=FOREGROUND_SEARCH_BUTTON,
                              border=0)
        keyMapButton.pack(expand=True,
                          side="left")
        oledButton = Button(headerFrame,
                            text="OLED",
                            height=100,
                            width=20,
                            bg=BACKGROUND_SEARCH_BUTTON,
                            activebackground=ACTIVEBACKGROUND_SEARCH_BUTTON,
                            activeforeground=FOREGROUND_SEARCH_BUTTON,
                            fg=FOREGROUND_SEARCH_BUTTON,
                            border=0)
        oledButton.pack(side="left",
                        expand=True)
        importButton = Button(headerFrame,
                              text="Import",
                              height=100,
                              width=20,
                              bg=BACKGROUND_SEARCH_BUTTON,
                              activebackground=ACTIVEBACKGROUND_SEARCH_BUTTON,
                              activeforeground=FOREGROUND_SEARCH_BUTTON,
                              fg=FOREGROUND_SEARCH_BUTTON,
                              border=0)
        importButton.pack(side="left",
                          expand=True)
        keyTesterButton = Button(headerFrame,
                                 text="Key Tester",
                                 height=100,
                                 width=20,
                                 bg=BACKGROUND_SEARCH_BUTTON,
                                 activebackground=ACTIVEBACKGROUND_SEARCH_BUTTON,
                                 activeforeground=FOREGROUND_SEARCH_BUTTON,
                                 fg=FOREGROUND_SEARCH_BUTTON,
                                 border=0)
        keyTesterButton.pack(side="left",
                             expand=True)
        settingsButton = Button(headerFrame,
                                text="Settings",
                                height=100,
                                width=20,
                                bg=BACKGROUND_SEARCH_BUTTON,
                                activebackground=ACTIVEBACKGROUND_SEARCH_BUTTON,
                                activeforeground=FOREGROUND_SEARCH_BUTTON,
                                fg=FOREGROUND_SEARCH_BUTTON,
                                border=0)
        settingsButton.pack(side="left",
                            expand=True)
