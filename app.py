"""
Run a saved model on your webcam using OpenCV.

Direct the filepath str on line 14 to the desired model
in this directory.

Execute this file to launch the video.
Press Q to quit or close the window.
"""
import cv2
import tensorflow as tf

# Load the model
model: tf.keras.Model = tf.keras.models.load_model("model_filepath")

def main() -> None:
    """
    Run the program.
    """
    # Select webcam
    # this might connect to your phone cam,
    # then try changing 1 to 0
    cap = cv2.VideoCapture(1)

    # video loop
    while True:
        # read frame from webcam
        ret, frame = cap.read()
        if not ret:
            break

        # TODO: process frame
        # remember to greyscale it
        ...

        # display frame
        cv2.imshow(model.name, frame)

        # quit video
        if cv2.waitKey(1) == ord('q'):
            break

    # terminate the program
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()