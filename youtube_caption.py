# pip3 install youtube-transcript-api
# pip3 install flair
# docker: docker-script-opensfm

# from pathlib import Path
# import flair
# flair.cache_root = "/your/path/.flair" # DOES NOT WORK
# flair.cache_root = Path("/your/path/.flair")# WORKS


from youtube_transcript_api import YouTubeTranscriptApi
srt = YouTubeTranscriptApi.get_transcript("zS2DFYKzVI0")

for sentence in srt:
    print(sentence)

sentence_arr = [sent['text'] for sent in srt]

sentence = ' '.join(sentence_arr)

import flair
from pathlib import Path
# import flair
flair.cache_root = Path("/home/user/flair_cache")# WORKS
sentiment_model = flair.models.TextClassifier.load('en-sentiment')
sentence = flair.data.Sentence(sentence)
sentiment_model.predict(sentence)
print(sentence)



