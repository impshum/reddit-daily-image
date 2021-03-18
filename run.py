import os
import praw
import schedule
from time import sleep
from random import choice
import configparser


config = configparser.ConfigParser()
config.read('conf.ini')
reddit_user = config['REDDIT']['reddit_user']
reddit_pass = config['REDDIT']['reddit_pass']
reddit_client_id = config['REDDIT']['reddit_client_id']
reddit_client_secret = config['REDDIT']['reddit_client_secret']
reddit_target_subreddit = config['REDDIT']['reddit_target_subreddit']
post_time = config['SETTINGS']['post_time']


reddit = praw.Reddit(
    username=reddit_user,
    password=reddit_pass,
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent='Reddit Daily Image (by u/impshum)'
)

sub = reddit.subreddit(target_subreddit)

in_dir = 'data/in/'
out_dir = 'data/out/'

x = 0


def set():
    global x
    x = 1


def main():
    dir = os.listdir(in_dir)
    all_images = len(dir)
    if all_images > 0:
        random_image = choice(dir)
        file_path_in = f'{in_dir}{random_image}'
        file_path_out = f'{out_dir}{random_image}'
        os.rename(file_path_in, file_path_out)
        title = os.path.splitext(random_image)
        title = title[0].replace('_', ' ')
        sub.submit(title, url=upload_image.link)
        print(f'{all_images} images remaining')
    else:
        set()


# schedule.every(1).seconds.do(main)
# schedule.every(10).minutes.do(main)
# schedule.every().hour.do(main)
schedule.every().day.at(post_time).do(main)
# schedule.every().monday.do(main)
# schedule.every().wednesday.at(post_time).do(main)

while True:
    schedule.run_pending()
    sleep(1)
    if x:
        print('No images')
        break
