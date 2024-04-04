from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()

recording = False


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
    <head>
        <title>Video Recorder</title>
    </head>
    <body>
        <h1>Video Recorder</h1>
        <video id="videoElement" width="640" height="480" autoplay></video><br>
        <button id="startButton" onclick="startRecording()">Start Recording</button>
        <button id="stopButton" onclick="stopRecording()" disabled>Stop Recording</button>

        <script>
            let videoElement = document.getElementById('videoElement');
            let startButton = document.getElementById('startButton');
            let stopButton = document.getElementById('stopButton');
            let mediaRecorder;
            let chunks = [];

            async function startRecording() {
                const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                videoElement.srcObject = stream;
                mediaRecorder = new MediaRecorder(stream);

                mediaRecorder.start();
                startButton.disabled = true;
                stopButton.disabled = false;

                mediaRecorder.ondataavailable = function (event) {
                    chunks.push(event.data);
                }
            }

            function stopRecording() {
                mediaRecorder.stop();
                startButton.disabled = false;
                stopButton.disabled = true;

                let blob = new Blob(chunks, { type: 'video/webm' });
                let url = window.URL.createObjectURL(blob);
                let a = document.createElement('a');
                a.href = url;
                a.download = 'recording.webm';
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
                chunks = [];
            }
        </script>
    </body>
    </html>
    """


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
