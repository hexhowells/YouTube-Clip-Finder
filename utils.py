import urllib.request
import json
import urllib
from youtube_transcript_api import YouTubeTranscriptApi as yt_api


def get_video_info(video_id):
	params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % video_id}
	url = "https://www.youtube.com/oembed"
	query_string = urllib.parse.urlencode(params)
	url = f'{url}?{query_string}'

	with urllib.request.urlopen(url) as response:
	    response_text = response.read()
	    data = json.loads(response_text.decode())
	    video_data = {}
	    video_data['title'] = data['title']
	    video_data['channel'] = data['author_name']
	    video_data['img_url'] = data['thumbnail_url']

	    return video_data



def normalise(text):
	return text.replace("'", "").lower()


def get_transcript(video_id):
	return yt_api.get_transcript(video_id)


def search_transcript(text, transcript):
	text = normalise(text)

	matching_clips = []
	for clip in transcript:
		if text in normalise(clip['text']):
			matching_clips.append(clip)

	return matching_clips 