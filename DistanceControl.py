import tkinter as tk
from tkinter import ttk


def set_transparent(window):
    window.configure(background='black')
    window.attributes("-alpha", 0.8)  # Set transparency level (0.0 to 1.0)


def slide_screenToBody_distance(*args):
    switch1_value = int(switch1.get() * 100)
    print("Switch 1:", switch1_value)
    slide_feature_distance_label.config(text=str(switch1_value * 2 + 100) + 'cm')
    return switch1_value


def zooming_screenToBody_distance(*args):
    switch2_value = int(switch2.get() * 100)
    print("Switch 2:", switch2_value)
    zoom_feature_distance_label.config(text=str(switch2_value * 2 + 100) + 'cm')
    return switch2_value


slide = 0


def check_slide_button_state():
    return slide


def enable_slide_feature(event):
    position = enable_slide.get()
    global slide
    slide = position
    if position == 1:
        enable_slide_switch_label.config(text="ON", bg="green")
    else:
        enable_slide_switch_label.config(text="OFF", bg="red")


zoom = 0


def check_zoom_button_state():
    return zoom


def enable_zooming_feature(event):
    position = enable_zoom.get()
    global zoom
    zoom = position
    if position == 1:
        enable_zoom_switch_label.config(text="ON", bg="green")
    else:
        enable_zoom_switch_label.config(text="OFF", bg="red")


brightness = 0


def check_brightness_button_state():
    return brightness


def enable_brightness_control_feature(event):
    position = enable_brightness.get()
    global brightness
    brightness = position
    if position == 1:
        enable_brightness_switch_label.config(text="ON", bg="green")
    else:
        enable_brightness_switch_label.config(text="OFF", bg="red")


tab_switch = 0


def check_tab_button_state():
    return tab_switch


def enable_switch_tab_feature(event):
    position = enable_tab.get()
    global tab_switch
    tab_switch = position
    if position == 1:
        enable_tab_switch_label.config(text="ON", bg="green")
    else:
        enable_tab_switch_label.config(text="OFF", bg="red")


def customize():
    root = tk.Tk()
    root.title("\U0001F4C4")
    root.iconbitmap("Presentation.ico")
    root.geometry("500x400")
    root.resizable(False, False)
    set_transparent(root)

    # Create a custom style with a transparent background
    style = ttk.Style()
    style.configure('Transparent.TFrame', background=root.cget('bg'))

    switch_frame = ttk.Frame(root, padding="10")
    switch_frame.place(x=340, y=40)

    # Distance control feature
    switch1_label = ttk.Label(root, text="Slide to adjust body to screen \ndistance for sliding feature",
                              background="black", foreground='white', font=('Helvetica', 8))
    switch1_label.place(x=30, y=35)

    global slide_feature_distance_label
    slide_feature_distance_label = ttk.Label(root, text='100cm',
                                             background="black", foreground='white', font=('Helvetica', 12))
    slide_feature_distance_label.place(x=240, y=40)

    global switch1  # making switch1 global so that it can be accessed in on_switch1_slide
    switch1 = ttk.Scale(switch_frame, from_=0, to=1, orient="horizontal", command=slide_screenToBody_distance)
    switch1.grid(row=0, column=1, padx=8, pady=4)

    switch2_label = ttk.Label(root, text="Slide to adjust body to screen \ndistance for zooming feature",
                              background='black', foreground="white", font=('Helvetica', 8))
    switch2_label.place(x=30, y=85)

    global zoom_feature_distance_label
    zoom_feature_distance_label = ttk.Label(root, text='100cm',
                                            background='black', foreground="white", font=('Helvetica', 12))
    zoom_feature_distance_label.place(x=240, y=90)

    global switch2  # making switch2 global so that it can be accessed in on_switch2_slide
    switch2 = ttk.Scale(switch_frame, from_=0, to=1, orient="horizontal", command=zooming_screenToBody_distance)
    switch2.grid(row=1, column=1, padx=8, pady=4)

    # Increase font size
    label_font = ('Helvetica', 12)  # Change the font family and size as needed

    # Slide feature           #############*********1.**********##################

    enable_slide_label = ttk.Label(root, text="Enable sliding control",
                                   background='black', foreground="white", font=label_font)
    enable_slide_label.place(x=30, y=155)

    global enable_slide
    enable_slide = tk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, length=50, showvalue=False, sliderlength=20,
                            command=enable_slide_feature, border=3)
    enable_slide.place(x=335, y=156)

    # Label to display the current state
    global enable_slide_switch_label
    enable_slide_switch_label = tk.Label(root, text="OFF", bg="red", fg="white", width=5, padx=10, border=3)
    enable_slide_switch_label.place(x=400, y=155)

    # zooming feature feature #############*********2.**********##################

    enable_zooming_label = ttk.Label(root, text="Enable zooming control",
                                     background='black', foreground="white", font=label_font)
    enable_zooming_label.place(x=30, y=205)
    global enable_zoom
    enable_zoom = tk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, length=50, showvalue=False, sliderlength=20,
                           command=enable_zooming_feature, border=3)
    enable_zoom.place(x=335, y=206)

    # Label to display the current state
    global enable_zoom_switch_label
    enable_zoom_switch_label = tk.Label(root, text="OFF", bg="red", fg="white", width=5, padx=10, border=3)
    enable_zoom_switch_label.place(x=400, y=205)

    # Brightness feature      #############*********3.**********##################
    enable_brightness_label = ttk.Label(root, text="Enable brightness control",
                                        background='black', foreground="white", font=label_font)
    enable_brightness_label.place(x=30, y=255)
    global enable_brightness
    enable_brightness = tk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, length=50, showvalue=False,
                                 sliderlength=20,
                                 command=enable_brightness_control_feature, border=3)
    enable_brightness.place(x=335, y=256)

    # Label to display the current state
    global enable_brightness_switch_label
    enable_brightness_switch_label = tk.Label(root, text="OFF", bg="red", fg="white", width=5, padx=10, border=3)
    enable_brightness_switch_label.place(x=400, y=255)

    # Tab switching feature   #############********4.***********##################
    enable_tab_label = ttk.Label(root, text="Enable tab switching control",
                                 background='black', foreground="white", font=label_font)
    enable_tab_label.place(x=30, y=305)
    global enable_tab
    enable_tab = tk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, length=50, showvalue=False, sliderlength=20,
                          command=enable_switch_tab_feature, border=3)
    enable_tab.place(x=335, y=306)

    # Label to display the current state
    global enable_tab_switch_label
    enable_tab_switch_label = tk.Label(root, text="OFF", bg="red", fg="white", width=5, padx=10, border=3)
    enable_tab_switch_label.place(x=400, y=305)

    def close():
        root.destroy()

    # Back button
    back_button = tk.Button(root, text='X', bg='black', fg='white', command=close)
    back_button.place(x=5, y=0)

    root.mainloop()


# customize()
