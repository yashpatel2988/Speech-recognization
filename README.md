Set Up Google Cloud Platform (GCP):

Create a GCP account if you don't have one.
Enable the Google Cloud Speech-to-Text API.
Set up authentication and obtain the necessary credentials.
Install Required Python Packages:

Install FastAPI for building the web API.
Install the Google Cloud Speech library for speech recognition.
Optionally, you may need other libraries for video processing and storage management.
Design User Interface:

Design a user interface for the web app using HTML, CSS, and JavaScript.
Include features such as camera access, start/stop recording buttons, and a display area for the recorded video.
Optionally, you can include language selection options and a progress indicator for storage usage.
Implement Backend with FastAPI:

Create routes in FastAPI to handle video recording, speech recognition, and video storage.
Implement endpoints for starting and stopping video recording, uploading videos, and transcribing speech.
Ensure that the backend handles language conversion from Hindi to English during speech recognition.
Integrate Camera Access:

Use browser APIs such as navigator.mediaDevices.getUserMedia to access the camera and microphone.
Implement logic to capture video and audio streams from the camera and microphone.
Perform Speech Recognition:

Use the Google Cloud Speech-to-Text API to transcribe speech from the recorded audio.
Send the audio data to the backend for processing and receive the transcription results.
Handle Video Storage:

Implement logic to manage video storage and enforce the maximum storage limit.
Store the recorded videos in a suitable storage solution, such as a file system or cloud storage.
Implement functionality for listing, viewing, and deleting recorded videos in the web dashboard.
Test the Application:

Test the web app to ensure that all features work as expected.
Record videos in Hindi, verify that they are transcribed to English correctly, and check storage management functionality.
Deploy the Web App:

Deploy the web app to a suitable hosting environment, such as a cloud platform or a web server.
Ensure that the deployment environment has the necessary resources and permissions to access GCP services and store videos.
Submit Videos for Review:

Record three vertical format videos showcasing the app's functionality and user interface.
Submit the videos for review, ensuring that they demonstrate the key features mentioned in the task description.
