import threading
import time
import tkinter as tk
from tkinter import ttk

import cv2
import mediapipe as mp

import Scroll
import Zooming
import Sliding
from CustomizePanel import check_stb_dis_zoom
from CustomizePanel import check_zoom_button_state
from CustomizePanel import check_scroll_button_state
from CustomizePanel import check_left_slide_button_state
from CustomizePanel import check_right_slide_button_state
from CustomizePanel import check_show_video_feed_button_state

X_STATE1 = 0
X_STATE2 = 0
FLAG = 0
_XY_SLIDE = False
_YX_SLIDE = False
_HAND_STATE = False

# remote_video_feed_url = "http://192.168.114.253:81/stream"


def check_hand_state():
    return _HAND_STATE


# Function to reset screen every 2 seconds
def reset_screen():
    global X_STATE1, X_STATE2, FLAG
    while True:
        if not check_hand_state():
            X_STATE1 = 0
            X_STATE2 = 0
            FLAG = 0
        time.sleep(3)


def set_transparent(window):
    window.configure(background='black')
    window.attributes("-alpha", 0.8)  # Set transparency level (0.0 to 1.0)


STOP = False


def stop():
    global STOP
    STOP = True


class HandGestureController:
    def __init__(self):
        self.camera_no = None
        self.root = tk.Tk()
        self.root.title("\U0001F4C4")
        self.root.iconbitmap("PresentationIcon.ico")
        self.root.geometry("400x200")
        self.root.resizable(False, False)
        set_transparent(self.root)

        """   The subsequent sections offer layouts and controls
              designed for the selection of a particular connected
              camera and the capture of its feed, tailored specifically 
              for enabling gesture-based interactions. 
        """

        def submit_text():
            submitted_text = url_text_entry_for_remote_camera_feed.get()
            if submitted_text == '0':
                self.camera_no = 0
            elif submitted_text == '1':
                self.camera_no = 1
            else:
                self.camera_no = submitted_text
            self.root.destroy()

        label = tk.Label(self.root, text="Choose camera EX: LOCAL(0), \n USB(1..),  URL(http://..) ", bg='black',
                         fg='white')
        label.place(x=80, y=20)
        url_text_entry_for_remote_camera_feed = ttk.Entry(self.root, width=20, font=('Arial', 12))
        submit_url_button = tk.Button(self.root, text="Submit", width=8, height=1, bg='blue',
                                      fg='white', command=submit_text)
        url_text_entry_for_remote_camera_feed.place(x=70, y=100)
        submit_url_button.place(x=155, y=150)
        self.root.mainloop()

        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = None

    def detect_hand_landmarks(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        hand1_start_x = None
        hand1_start_y = None
        hand2_start_x = None
        hand2_start_y = None

        if results.multi_hand_landmarks:
            for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
                x_cords = [landmark.x for landmark in hand_landmarks.landmark]
                y_cords = [landmark.y for landmark in hand_landmarks.landmark]

                if i == 0:
                    hand1_start_x = min(x_cords)
                    hand1_start_y = min(y_cords)
                else:
                    hand2_start_x = min(x_cords)
                    hand2_start_y = min(y_cords)

                for landmark in hand_landmarks.landmark:
                    x, y, z = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]), landmark.z
                    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

        # check if zoom button is enable to perform the feature
        if check_zoom_button_state():
            if hand1_start_x is not None and hand2_start_x is not None or hand1_start_y is not None and \
                    hand2_start_y is not None:
                axis_hands_pixel_difference = max(abs(hand1_start_x * frame.shape[1] - hand2_start_x * frame.shape[1]),
                                                  abs(hand1_start_y * frame.shape[1] - hand2_start_y * frame.shape[1]))
                # print("screen-to-body-distance", check_stb_dis_zoom())
                if axis_hands_pixel_difference + check_stb_dis_zoom() >= 200:
                    Zooming.zoom(axis_hands_pixel_difference)

        if check_show_video_feed_button_state():
            cv2.imshow('Hand Landmarks', frame)

        # If camara is detecting two hands then disable one hand feature
        # by returning None to the one hand feature
        if hand1_start_x is not None and hand2_start_x is not None:
            return [None, None, None, None]

        # scroll feature it will be enabled only when one hand is detecting
        if hand1_start_y is not None:
            # check scroll button is on or off
            if check_scroll_button_state():
                value = hand1_start_y * frame.shape[1]
                if value < 350:
                    if value < 150:
                        Scroll.scroll_up_to_down()
                    else:
                        Scroll.scroll_down_to_up()

        if hand1_start_x is not None:
            hand1_start_x = hand1_start_x * frame.shape[1]

        if hand1_start_y is not None:
            hand1_start_y = hand1_start_y * frame.shape[1]

        if hand2_start_x is not None:
            hand2_start_x = hand2_start_x * frame.shape[1]

        if hand2_start_x is not None:
            hand2_start_y = hand2_start_x * frame.shape[1]

        print(list([hand1_start_x, hand1_start_y, hand2_start_x, hand2_start_y]))
        return [hand1_start_x]

    def main(self):
        global X_STATE1, X_STATE2, _YX_SLIDE, _XY_SLIDE, _HAND_STATE
        cap = cv2.VideoCapture(self.camera_no)  # Adjusted variable name to 'camera_no' for consistency

        # Create a thread for the reminder function
        reset_screen_thread = threading.Thread(target=reset_screen)
        reset_screen_thread.daemon = True  # Set as daemon, so it automatically exits when the main program exits
        # Start the reminder thread
        reset_screen_thread.start()

        global FLAG
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)

            cords_of_one_hands = self.detect_hand_landmarks(frame)

            if cords_of_one_hands[0] is None:
                _HAND_STATE = False
                print(FLAG)
            else:
                _HAND_STATE = True

            # If both left and right sliding feature enable
            check_LSBS = check_left_slide_button_state()
            check_RSBS = check_right_slide_button_state()

            if cords_of_one_hands[0] is not None:
                if check_LSBS and check_RSBS:
                    if cords_of_one_hands[0] < 250 and (FLAG == 0 or FLAG == 1):
                        FLAG = 1
                        print(FLAG)
                        _XY_SLIDE = True

                    elif cords_of_one_hands[0] > 350 and (FLAG == 0 or FLAG == 2):
                        FLAG = 2
                        print(FLAG)
                        _YX_SLIDE = True

                # If left sliding feature enable

                elif check_LSBS:
                    if cords_of_one_hands[0] > 350:
                        _YX_SLIDE = True

                # If right sliding feature enable
                elif check_RSBS:
                    if cords_of_one_hands[0] < 250:
                        _XY_SLIDE = True

                if cords_of_one_hands[0] < 250 and _YX_SLIDE == True:
                    Sliding.slide_right_to_left()
                    _YX_SLIDE = False

                elif cords_of_one_hands[0] > 350 and _XY_SLIDE == True:
                    Sliding.slide_left_to_right()
                    _XY_SLIDE = False

            # if cords_of_one_hands[0] is not None and 200 > cords_of_one_hands[0] > 20:         # EXPERIMENTAL LOGS
            #     if X_STATE2 == 1:
            #         Sliding.slide_right_to_left()
            #         X_STATE1 = 0
            #         X_STATE2 = 0
            #         sleep(1)
            #     else:
            #         X_STATE1 = 1
            #
            # if cords_of_one_hands[0] is not None and 600 > cords_of_one_hands[0] > 350:
            #     if X_STATE1 == 1:
            #         Sliding.slide_left_to_right()
            #         X_STATE1 = 0
            #         X_STATE2 = 0
            #         sleep(1)
            #     else:
            #         X_STATE2 = 1

            if STOP:
                break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def execute(self):
        self.hands = self.mp_hands.Hands()
        self.main()


# Defining execute function outside the class
def execute():
    hand_gesture_controller = HandGestureController()
    hand_gesture_controller.execute()

#
# # Call execute function
# execute()
