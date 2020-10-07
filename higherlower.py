#!/usr/bin/env python
import random
from youtube_api import YouTubeDataAPI

class Video:
    def __init__(self, yt):
        terms = open('./terms.txt').readlines()
        mdata = yt.get_video_metadata(yt.search(q=terms[random.randint(0,len(terms)-1)].strip(),max_results=20)[random.randint(0,19)]['video_id'])
        self.title, self.views, self.thumbnail_link, self.creator = mdata['video_title'], int(mdata['video_view_count']), mdata['video_thumbnail'], mdata['channel_title']
        
class Game:
    def loop(self, target):
        score = 0
        yt = YouTubeDataAPI(YOURAPIKEY)
        while score < target:
            print('==========================================================================')
            Vid1 = Video(yt)
            print(f'1. {Vid1.title} by {Vid1.creator} has {Vid1.views} views.')
            Vid2 = Video(yt)
            print(f'2. {Vid2.title} by {Vid2.creator}.')
            if (input('Video #2\'s views compared to Video #1 will be ? (Higher/Lower) ?\n').lower() == 'higher') == (Vid2.views > Vid1.views):
                print('\nCorrect!\n')
                score += 1
            else:
                print('\nIncorrect! Resetting the score!\n')
                score = 0
            
            print(f'{Vid1.creator}\'s video has {Vid1.views} views while {Vid2.creator}\'s video has {Vid2.views}')
            print('SCORE:',score)
            print()
        print('Congrats! You win!')

target = int(input("Enter the score you want to achieve: "))
Game().loop(target)
