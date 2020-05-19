## Reddit Daily Image

A scheduled script to upload images to Imgur then post to Reddit using the filename as the title (set and forget).

### Instructions

-   Install requirements `pip install -r requirements.txt`
-   Create Reddit (script) app at <https://www.reddit.com/prefs/apps/> and get keys
-   Create Imgur app at <https://api.imgur.com/oauth2/addclient> and get keys
-   Edit conf.ini with your details
-   Put images into data/in/
-   Rename images with desired title replacing spaces with underscores e.g. Big_Massive_Title_Twizzler.jpg
-   Run it `python run.py`

### Notes

-   If you want to change the schedule have a look at the bottom of run.py (default - Daily)
-   I will not be held responsible for any bad things that might happen to you or your Reddit account whilst using this bot. Follow Reddiquette and stay safe.
