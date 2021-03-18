import os
import praw
import schedule
import random
import time
import configparser
import threading

try:
    import queue
except ImportError:
    import Queue as queue


config = configparser.ConfigParser()
config.read('conf.ini')
reddit_user = config['REDDIT']['reddit_user']
reddit_pass = config['REDDIT']['reddit_pass']
reddit_client_id = config['REDDIT']['reddit_client_id']
reddit_client_secret = config['REDDIT']['reddit_client_secret']
reddit_target_subreddit = config['REDDIT']['reddit_target_subreddit']
post_time = config['SETTINGS']['post_time']

image_in_dir = 'images/'
stopper = 0


def set_stopper():
    global stopper
    stopper = 1


reddit = praw.Reddit(
    username=reddit_user,
    password=reddit_pass,
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent='Reddit Daily Image (by u/impshum)'
)

reddit.validate_on_submit = True


def get_random_image(dir):
    images = [x for x in os.listdir(dir) if x.endswith(
        ('jpg', 'jpeg', 'png', 'gif'))]

    if not images:
        set_stopper()
        print('No images')
        return

    image = random.choice(images)
    title = os.path.splitext(image)[0].replace('_', ' ')
    return {'image': image, 'title': title}


def runner():
    while 1:
        job_func = jobqueue.get()
        job_func()
        jobqueue.task_done()
        if stopper:
            break


def main():
    random_image = get_random_image(image_in_dir)
    if random_image:
        title = random_image['title']
        image = os.path.abspath(image_in_dir + random_image['image'])
        reddit.subreddit(reddit_target_subreddit).submit_image(title, image)
        os.remove(image)
        print(title)


jobqueue = queue.Queue()

# schedule options
# schedule.every(10).seconds.do(jobqueue.put, main)
# schedule.every(3).minutes.do(jobqueue.put, main)
# schedule.every().hour.do(jobqueue.put, main)
# schedule.every().monday.do(jobqueue.put, main)

schedule.every().day.at(post_time).do(jobqueue.put, main)

worker_thread = threading.Thread(target=runner)
worker_thread.start()


while True:
    schedule.run_pending()
    time.sleep(1)
    if stopper:
        worker_thread.join()
        break
