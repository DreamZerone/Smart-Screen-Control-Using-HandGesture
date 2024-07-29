from time import sleep
import cv2
import mediapipe as mp


mp_hands = mp.solutions.hands
hands = mp_hands.Hands()


# Initialize video capture
cap = cv2.VideoCapture(0)
i = 0
while True:
    print("Wel")
    if i > 1:
        break
    sleep(1)
    i += 1

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame.")
        break

    # Convert the image to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            for landmark in hand_landmarks.landmark:
                # Get the coordinates of each landmark
                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    # Display the frame
    cv2.imshow('Hand Detection', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
