from flask import Flask, request, jsonify
from flask import render_template
import utils

app = Flask(__name__, static_url_path="")


@app.route("/")
def home(name=None):
	return render_template("index.html", name=name)


@app.route('/find-video', methods = ['POST', 'GET'])
def find_video():
	if request.method == 'POST':
		video_url = request.form['video-link']
		video_id = video_url.split("v=")[1]
		video_metadata = utils.get_video_info(video_id)
		return jsonify(video_metadata)
	else:
		return 'success'


@app.route('/find-clips', methods = ['POST', 'GET'])
def find_clip():
	if request.method == 'POST':
		video_url = request.form['video-link']
		search_text = request.form['search-text']

		video_id = video_url.split("v=")[1]
		transcript = utils.get_transcript(video_id)
		clips = utils.search_transcript(search_text, transcript)

		return jsonify(clips)
	else:
		return 'success'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)