import tkinter as tk
from tkinter import ttk

slide_distance = 0


def check_stb_dis_slide():  # check screen-to-body distance for slide
    return slide_distance


def slide_screenToBody_distance(*args):
    global slide_distance
    slide_distance = int(switch1.get() * 100) * 2 + 100
    # print("Switch 1:", slide_distance)
    slide_feature_distance_label.config(text=str(slide_distance) + 'cm')


zoom_distance = 0


def check_stb_dis_zoom():  # check screen-to-body distance for zoom
    return zoom_distance


def zooming_screenToBody_distance(*args):
    global zoom_distance
    zoom_distance = int(switch2.get() * 100) * 2 + 100
    # print("Switch 2:", zoom_distance)
    zoom_feature_distance_label.config(text=str(zoom_distance) + 'cm')


left_slide = 0


def check_left_slide_button_state():
    return left_slide


def enable_left_slide_feature(event):
    position = enable_left_slide.get()
    global left_slide
    left_slide = position
    if position == 1:
        enable_left_slide_switch_label.config(text="ON", bg="green")
    else:
        enable_left_slide_switch_label.config(text="OFF", bg="red")


right_slide = 0


def check_right_slide_button_state():
    return right_slide


def enable_right_slide_feature(event):
    position = enable_right_slide.get()
    global right_slide
    right_slide = position
    if position == 1:
        enable_right_slide_switch_label.config(text="ON", bg="green")
    else:
        enable_right_slide_switch_label.config(text="OFF", bg="red")


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


scroll_switch_state = 0


def check_scroll_button_state():
    return scroll_switch_state


def enable_scroll_feature(event):
    position = enable_scroll.get()
    global scroll_switch_state
    scroll_switch_state = position
    if position == 1:
        enable_scroll_switch_label.config(text="ON", bg="green")
    else:
        enable_scroll_switch_label.config(text="OFF", bg="red")


show_video_feed_switch_state = 0


def check_show_video_feed_button_state():
    return show_video_feed_switch_state


def enable_show_video_feed_feature(event):
    position = enable_show_video_feed.get()
    global show_video_feed_switch_state
    show_video_feed_switch_state = position
    if position == 1:
        enable_show_video_feed_switch_label.config(text="ON", bg="green")
    else:
        enable_show_video_feed_switch_label.config(text="OFF", bg="red")


def set_transparent(window):
    window.configure(background='black')
    window.attributes("-alpha", 0.8)  # Set transparency level (0.0 to 1.0)


def customize():
    root = tk.Tk()
    root.title("\U0001F4C4")
    root.iconbitmap("PresentationIcon.ico")
    root.geometry("1000x500")
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

    # left slide feature           #############*********1.1**********##################

    enable_left_slide_label = ttk.Label(root, text="Enable left sliding control",
                                        background='black', foreground="white", font=label_font)
    enable_left_slide_label.place(x=30, y=155)

    global enable_left_slide
    enable_left_slide = tk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, length=50, showvalue=False, sliderlength=20,
                                 command=enable_left_slide_feature, border=3)
    enable_left_slide.place(x=335, y=156)

    # Label to display the current state
    global enable_left_slide_switch_label
    enable_left_slide_switch_label = tk.Label(root, text="OFF", bg="red", fg="white", width=5, padx=10, border=3)
    enable_left_slide_switch_label.place(x=400, y=155)

    # right slide feature           #############*********1.2**********##################

    enable_right_slide_label = ttk.Label(root, text="Enable right sliding control",
                                         background='black', foreground="white", font=label_font)
    enable_right_slide_label.place(x=30, y=205)

    global enable_right_slide
    enable_right_slide = tk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, length=50, showvalue=False,
                                  sliderlength=20,
                                  command=enable_right_slide_feature, border=3)
    enable_right_slide.place(x=335, y=206)

    # Label to display the current state
    global enable_right_slide_switch_label
    enable_right_slide_switch_label = tk.Label(root, text="OFF", bg="red", fg="white", width=5, padx=10, border=3)
    enable_right_slide_switch_label.place(x=400, y=205)

    # zooming feature feature #############*********2.**********##################

    enable_zooming_label = ttk.Label(root, text="Enable zooming control",
                                     background='black', foreground="white", font=label_font)
    enable_zooming_label.place(x=30, y=255)
    global enable_zoom
    enable_zoom = tk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, length=50, showvalue=False, sliderlength=20,
                           command=enable_zooming_feature, border=3)
    enable_zoom.place(x=335, y=256)

    # Label to display the current state
    global enable_zoom_switch_label
    enable_zoom_switch_label = tk.Label(root, text="OFF", bg="red", fg="white", width=5, padx=10, border=3)
    enable_zoom_switch_label.place(x=400, y=255)

    # Brightness feature      #############*********3.**********##################
    enable_brightness_label = ttk.Label(root, text="Enable brightness control",
                                        background='black', foreground="white", font=label_font)
    enable_brightness_label.place(x=30, y=305)
    global enable_brightness
    enable_brightness = tk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, length=50, showvalue=False,
                                 sliderlength=20,
                                 command=enable_brightness_control_feature, border=3)
    enable_brightness.place(x=335, y=306)

    # Label to display the current state
    global enable_brightness_switch_label
    enable_brightness_switch_label = tk.Label(root, text="OFF", bg="red", fg="white", width=5, padx=10, border=3)
    enable_brightness_switch_label.place(x=400, y=305)

    # Tab switching feature   #############********4.***********##################
    enable_tab_label = ttk.Label(root, text="Enable tab switching control",
                                 background='black', foreground="white", font=label_font)
    enable_tab_label.place(x=30, y=355)

    global enable_tab
    enable_tab = tk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, length=50, showvalue=False, sliderlength=20,
                          command=enable_switch_tab_feature, border=3)
    enable_tab.place(x=335, y=356)

    # Label to display the current state
    global enable_tab_switch_label
    enable_tab_switch_label = tk.Label(root, text="OFF", bg="red", fg="white", width=5, padx=10, border=3)
    enable_tab_switch_label.place(x=400, y=355)

    # Scrolling feature   #############********4.***********##################
    enable_scroll_label = ttk.Label(root, text="Enable scroll control",
                                    background='black', foreground="white", font=label_font)
    enable_scroll_label.place(x=30, y=405)

    global enable_scroll
    enable_scroll = tk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, length=50, showvalue=False, sliderlength=20,
                             command=enable_scroll_feature, border=3)
    enable_scroll.place(x=335, y=405)

    # Label to display the current state
    global enable_scroll_switch_label
    enable_scroll_switch_label = tk.Label(root, text="OFF", bg="red", fg="white", width=5, padx=10, border=3)
    enable_scroll_switch_label.place(x=400, y=405)

    # Show video feed   #############********5.***********##################
    show_video_feed = ttk.Label(root, text="Enable to see video feed",
                                background='black', foreground="white", font=label_font)
    show_video_feed.place(x=500, y=100)

    global enable_show_video_feed
    enable_show_video_feed = tk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, length=80, showvalue=False,
                                      sliderlength=20, command=enable_show_video_feed_feature, border=3)
    enable_show_video_feed.place(x=800, y=100)

    # Label to display the current state
    global enable_show_video_feed_switch_label
    enable_show_video_feed_switch_label = tk.Label(root, text="OFF", bg="red", fg="white", width=5, padx=10, border=3)
    enable_show_video_feed_switch_label.place(x=900, y=100)

    video_feed = tk.Label(root, text="Video Feed", background='yellow')
    video_feed.place(x=550, y=200)
    video_feed.config(width=40, height=10)

    def close():
        root.destroy()

    # Back button
    back_button = tk.Button(root, text='X', bg='black', fg='white', command=close)
    back_button.place(x=5, y=0)

    root.mainloop()

# customize()
