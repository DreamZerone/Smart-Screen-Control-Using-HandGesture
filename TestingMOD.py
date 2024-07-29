from time import sleep

import cv2
import mediapipe as mp

# Initialize mediapipe hands module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils


# Function to detect and draw landmarks of the hand
def detect_hand_landmarks(frame):
    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    results = hands.process(rgb_frame)
    a = [0]*2
    b = [0]*2

    # If hands are detected, draw landmarks
    if results.multi_hand_landmarks:
        for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
            # Store the starting top position of X-axis for each hand
            x_cords = [landmark.x for landmark in hand_landmarks.landmark]
            y_cords = [landmark.y for landmark in hand_landmarks.landmark]
            if i == 0:
                # Hand1
                a[0] = min(x_cords)
                a[1] = max(x_cords)
            else:
                # Hand2
                b[0] = min(x_cords)
                b[1] = max(x_cords)

            # Draw connections between the landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the resulting frame
    print(a)
    print(b)
    sleep(2)
    cv2.imshow('Hand Landmarks', frame)


# Main function
def main():
    # Open webcam
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Flip frame horizontally
        frame = cv2.flip(frame, 1)

        # Detect hand coordinates
        detect_hand_landmarks(frame)

        # Exit loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Initialize mediapipe hands module
    hands = mp_hands.Hands()

    main()
