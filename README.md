# OpenCV Rolandinho eye detection

This Python script processes a series of frames from input images, detects eyes using the Haar cascade classifier, and annotates the frames with rectangles and labels for the detected eyes on Rolandinho photos. It utilizes the OpenCV library for image processing.

## Usage

1. Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

2. Prepare the input images:

    - Place the input images in a directory and specify the path to that directory in the `images_path` variable.
    - The input images should follow the naming convention `img_{frame_count}.jpg`, where `{frame_count}` is the index of the frame.

3. Configure the output path:

    - Specify the path where the processed frames will be saved by setting the `output_path` variable.

4. Run the script:

```bash
python src/main.py
```

_⚠️ Run python from the root directory of the project._

## Runtime

The script performs the following steps:

1. Initialize the frame count.

2. Iterate through the input images and process each frame:

    - Read the frame from the file.
    - Process the frame by detecting eyes and annotating them.
    - Display the frame.
    - Save the frame to the output path.

3. Increment the frame count.

4. When there are no more frames to process, the script terminates.

## Dependencies

The script relies on the following dependencies:

-   OpenCV (cv2): Used for image processing and visualization and for loading the Haar cascade classifier for eye detection.

## Notes

-   The Haar cascade classifier for eye detection is loaded from the `haarcascade_eye.xml` file provided by OpenCV.
-   The processed frames are displayed in separate windows and saved in [output folder](output), and the script waits for a key press before proceeding to the next frame. Once all frames have been processed, the script terminates.
