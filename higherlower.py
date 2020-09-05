import random
from youtube_api import YouTubeDataAPI

class Video:
    def __init__(self, yt):
        terms = open('terms.txt').readlines()
        mdata = yt.get_video_metadata(yt.search(q=terms[random.randint(0,len(terms)-1)].strip(),max_results=20)[random.randint(0,19)]['video_id'])
        self.title, self.views, self.thumbnail_link, self.creator = mdata['video_title'], int(mdata['video_view_count']), mdata['video_thumbnail'], mdata['channel_title']
class Game:
    def loop(self):
        score = 0
        yt = YouTubeDataAPI('YOURAPIKEY')
        while score < 20:
            print('==========================================================================')
            pv_video = Video(yt)
            print(f'{pv_video.title} by {pv_video.creator} has {pv_video.views} views.')
            game_video = Video(yt)
            print(f'{game_video.title} by {game_video.creator}.')
            if (input('Higher or Lower?\n').lower() == 'higher') == (game_video.views > pv_video.views):
                print('Yay')
                score += 1
            else:
                print('Nah')
                score = 0
            print('SCORE:',score)
        print('You win!')
Game().loop()