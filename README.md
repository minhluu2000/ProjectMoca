# ProjectMoca
 Using OpenCV and its highly trained facial features model (Viola Jones Algorithm), this simple software tracks your face and projects that position on the screen with a mouse cursor. Furthermore, clapping is used for left and right mouse inputs and voice recognition is used for keyboard input.

 After being inspired by a friend who challenged me to play Yuumi, a character in League of Legends, without a mouse and keyboard (a meme that the character is usually associated with), I decided to make this idea a reality. Further digging, I started to realize this can hopefully improve computer's accessibility of people with disability.



# Instruction
 1. Install [Anaconda](https://www.anaconda.com/).
 2. Create a virtualenv with `conda create --name [ProjectName] python=[version]`. Activate using `activate [ProjectName]`.
 3. Install all necessasry libraries via requirements.txt.
 4. Install dlib with `conda install -c conda-forge dlib`.
 5. Go to face_detection.py inside the ProjectMoca folder and change rescale resolution. This is for scaling from the webcam to the projected monitor (Huge thanks for the tutorial from [Justin Mitchel](https://www.codingforentrepreneurs.com/blog/open-cv-python-change-video-resolution-or-scale))


