# pip3 install youtube-transcript-api
# pip3 install flair
# docker: docker-script-opensfm

# from pathlib import Path
# import flair
# flair.cache_root = "/your/path/.flair" # DOES NOT WORK
# flair.cache_root = Path("/your/path/.flair")# WORKS


# from youtube_transcript_api import YouTubeTranscriptApi
# srt = YouTubeTranscriptApi.get_transcript("zS2DFYKzVI0")

# for sentence in srt:
#     print(sentence)

# sentence_arr = [sent['text'] for sent in srt]

# sentence = ' '.join(sentence_arr)

# import flair
# from pathlib import Path
# # import flair
# flair.cache_root = Path("/home/user/flair_cache")# WORKS
# sentiment_model = flair.models.TextClassifier.load('en-sentiment')
# sentence = flair.data.Sentence(sentence)
# sentiment_model.predict(sentence)
# print(sentence)

from youtube_transcript_api import YouTubeTranscriptApi
from youtubesearchpython import *
import time
import flair
from pathlib import Path
import json
import requests
import re
flair.cache_root = Path("/home/user/flair_cache")# WORKS
sentiment_model = flair.models.TextClassifier.load('en-sentiment')
searchText_List = ['tesla news', 'tesla stock', 'apple news', 'apple stock']

for searchText in searchText_List:
    
    customSearch = CustomSearch(searchText, VideoSortOrder.uploadDate, limit = 20)

    print(customSearch.result())



    for result in customSearch.result()['result']:
        try:
            print("------------------")
            print(result['id'])
            print(result['title'])
            srt = YouTubeTranscriptApi.get_transcript(result['id'])
            sentence_arr = [sent['text'] for sent in srt]
            sentence = ' '.join(sentence_arr)
            sentence = re.sub(r"[^a-zA-Z0-9]"," ",sentence)
            # print(sentence)
            sentence_result = flair.data.Sentence(sentence)
            sentiment_model.predict(sentence_result)
            print(sentence_result.labels)
            

            score_string = ""
            if sentence_result.labels[0].value == 'NEGATIVE':
                score_string = "-"
            score_string = score_string + str(sentence_result.labels[0].score)

            my_data = {
                'searchText':searchText,
                'title':result['title'],
                'is_transcript':'Y',
                'text':sentence,
                'score': float(score_string),
                'urlId':result['id']
            }
            print(my_data)

            my_headers = {'Content-Type': 'application/json'}
            r = requests.post('http://10.1.1.9:7002/demo/api/text', data = json.dumps(my_data), headers = my_headers)
            
        

            time.sleep(10)
        except:
            print("cannot get subtitles")
            time.sleep(10)



