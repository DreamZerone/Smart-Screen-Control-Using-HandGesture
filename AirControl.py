import tkinter as tk
import threading
import CustomizePanel
import GestureControl


def set_transparent(window):
    window.configure(background='black')
    window.attributes("-alpha", 0.8)  # Set transparency level (0.0 to 1.0)


class SmartPresentationApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("\U0001F4C4")
        self.root.iconbitmap("PresentationIcon.ico")
        self.root.geometry("350x450")
        self.root.resizable(False, False)

        # Call set_transparent() to make the window transparent
        set_transparent(self.root)

        def button1_action():
            self.button1.configure(bg='red', fg='white', text='close\t\t')
            threading.Thread(target=GestureControl.execute).start()

        def button3_action():
            print("Button 3 clicked")

        def button2_action():
            self.button2.configure(bg='red', fg='white', text='close\t\t')
            CustomizePanel.customize()

        def destroy_all_windows():
            self.root.destroy()
            GestureControl.stop()

        self.label1 = tk.Label(self.root, text='Smart Presentation', bg='black', fg='white', font=('Arial', 12))
        self.label1.place(x=68, y=20)
        self.button1 = tk.Button(self.root, text="Enable Feature\t", command=button1_action, bg='black',
                                 fg='white', border=1)
        self.button1.place(x=90, y=120)
        self.button1.config(border=5)
        self.button2 = tk.Button(self.root, text="Customize\t", command=button2_action, bg='black', fg='white',
                                 border=5)
        self.button2.place(x=90, y=175)
        self.button3 = tk.Button(self.root, text="READme_\t\t", command=button3_action, bg='black', fg='white')
        self.button3.place(x=180, y=380)

        # Bind the destroy_all_windows function to the window closing event
        self.root.protocol("WM_DELETE_WINDOW", destroy_all_windows)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = SmartPresentationApp()
    app.run()
