from flask import Flask, request, jsonify,send_file
from flask_cors import CORS 
from pytube import YouTube

app = Flask(__name__)
CORS(app, resources={
    r"/download_audio": {"origins": ["https://mp3downlaoder.vercel.app"]},
    r"/download_video": {"origins": ["https://mp3downlaoder.vercel.app", "chrome-extension://aemegkonfbajfofocedalcoicnfkgcjk"]}
})

@app.route('/download_audio', methods=['POST'])
def download_audio():
    try:
        data = request.get_json()
        link = data.get('link')
        youtube_object = YouTube(link)
        audio_stream = youtube_object.streams.filter(only_audio=True).first()
        audio_stream.download()
        return jsonify({'message': 'Audio download completed successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/download_video', methods=['POST'])
def download_video():
    try:
        data = request.get_json()
        link = data.get('link')
        youtube_object = YouTube(link)
        video_stream = youtube_object.streams.get_highest_resolution()
        video_stream.download()
        return jsonify({'message': 'Video download completed successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
