"""
    Stage: Development-01
    @author: Emine Esin Yılmaz, 120200059
    @author: Selin Yılmaz, 119203057

    Stage: Development-02
    @author: Amin habiballah , 119202002
    @author: Janberk Özsezer, 120202040

    Stage: Code Review
    @author: Omar Al-Shareef, 119200019
    @author: Batıkan Yılmaz , 120200036

"""

import tkinter as tk
class LoginWindow:
    # constructor
    def __init__(self):
        self.window = tk.Tk()

        self._initializeGUI()
        self._addGUIElementsToFrame()

        # start the GUI frame
        self.window.mainloop()


    """
        Initialize GUI elements. If it is necessary, you can add
        more elements.
        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """
    def _initializeGUI(self):
        self.lbl01 = tk.Label(text="Username or e-mail")
        self.lbl02 = tk.Label(text="Password")

        self.txt01 = tk.Entry()
        self.txt02 = tk.Entry(show="*")

        self.btn01 = tk.Button(text="Reset Password")
        self.btn02 = tk.Button(text="Login")

        self.btn01.bind("<Button-1>", self.handle_click)
        self.btn02.bind("<Button-1>", self.handle_click2)


    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.lbl01.grid(row=0, column=0, padx=10, pady=5)
        self.txt01.grid(row=0, column=1, padx=10, pady=5)

        self.lbl02.grid(row=1, column=0, padx=10, pady=5)
        self.txt02.grid(row=1, column=1, padx=10, pady=5)

        self.btn01.grid(row=2, column=0, padx=10, pady=5)
        self.btn02.grid(row=2, column=1, padx=10, pady=5)


    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.
        :param event: action event for detecting which button is clicked
    """

    def handle_click(self, event):
        window2 = tk.Tk()
        window2.mainloop()
        pass

    def handle_click2(self, event):
        self.window.destroy()
        window3 = tk.Tk()

        window3.geometry('900x900')
        self.webpage()
        self.elements()
        window3.mainloop()
        pass
    def webpage(self):
        self.lbl02 = tk.Label(text="Forum X")
        self.btn = tk.Button(text="Search")
    def elements(self):
        self.lbl02.grid(row=1, column=0, padx=10, pady=5)
        self.btn.grid(row=2, column=0, padx=10, pady=5)



# main method for testing the application
if __name__ == "__main__":
    LoginWindow()