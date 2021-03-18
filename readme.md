## Reddit Daily Image Bot (v3)

A scheduled script to upload images to Reddit using the filename as the title (set and forget).

![](r.jpg)

### Instructions

-   Install requirements `pip install -r requirements.txt`
-   Create Reddit (script) app at <https://www.reddit.com/prefs/apps/> and get keys
-   Edit conf.ini with your details
-   Put images into images folder
-   Rename images with desired title replacing spaces with underscores e.g. Big_Massive_Title_Twizzler.jpg
-   Run it `python run.py`

### Notes

-   Images will be deleted after posting. You have been warned!
-   If you want to change the schedule, to something other than daily, have a look at the bottom of run.py (default - Daily)
-   I will not be held responsible for any bad things that might happen to you or your Reddit account whilst using this bot. Follow Reddiquette and stay safe.
