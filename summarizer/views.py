from django.shortcuts import render, redirect
from youtube_transcript_api import YouTubeTranscriptApi
import math
# from transformers import pipeline
from keybert import KeyBERT
# from IPython.display import YouTubeVideo

# Create your views here.

def home(request):
    kw_model = KeyBERT()
    if request.method == "POST":
        link= request.POST['youtubeLink']
        video_id = link.split("=")[1]
        if '&' in video_id:
            video_id=video_id.split("&")[0]
        # Pre trained tranformer-
        
        important_segments = []
        srt = YouTubeTranscriptApi.get_transcript(video_id)
        paragraph = ' '.join(i['text'] for i in srt)
        
        
        keywords = kw_model.extract_keywords(paragraph, keyphrase_ngram_range=(1, 1), stop_words='english', use_maxsum=True, nr_candidates=20, top_n=10)
        
        for segment in srt:
            segment_text = segment['text'].lower()
            for keyword,_ in keywords:
                if keyword.lower() in segment_text:
                    start_time = segment['start']
                    end_time = start_time + segment['duration']
                    important_segments.append((start_time, end_time))
                    break
        
        adjusted_segments = [(math.floor(start), math.ceil(end)) for start, end in important_segments]
        merged = [adjusted_segments[0]]
        for current_start, current_end in adjusted_segments[1:]:
            last_start, last_end = merged[-1]
            if current_start <= last_end:
                merged[-1] = (last_start, max(last_end, current_end))
            else:
                merged.append((current_start, current_end))
                       
        # important_segments = [(15, 25),(30, 45)]
        return render(request, 'home.html', {'video_id': video_id,'segments': merged})
    return render(request, 'home.html')