from flask import Flask,render_template,request
import yt_dlp
app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('yt_url')
        print("Received URL:", url)

        ydl_opts = {
                'format': 'best',
                'outtmpl': 'downloads/%(title)s.%(ext)s'
            }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                video_title = info_dict.get('title', None)
                return f"Video downloaded: {video_title}"
        except Exception as e:
            return f"Error: {str(e)}"
    return render_template('index.html')









if __name__ == '__main__':
    app.run(debug=True)