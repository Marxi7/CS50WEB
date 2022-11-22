# CS50 Wev Programming with Python & Javascript
Here, you will find all of my projects completed for CS50's Web programming with Python and Javascript by C50.
<hr>

### Projects description:

#### Project 0 - Search:
Front-end site made with HTML and CSS to replicate Google Search, Google Image Search, and Google Advanced Search.<br>
Instructions [Here](https://cs50.harvard.edu/web/2020/projects/0/search/)<br>
Demo video:  <https://youtu.be/lmyRzcm066w>

#### Project 1 - Wiki:
Mini Clone of Wikipedia with a markdown system implemented.<br>
Instructions [Here](https://cs50.harvard.edu/web/2020/projects/1/wiki/)<br>
Demo video:  <https://youtu.be/4OTYymc4-gA>

#### Project 2 - Commerce:
Auction site that will allow users to post, edit auction listings, place bids on listings, comment on those listings, and add listings they like to their “watchlist.”<br>
Instructions [Here](https://cs50.harvard.edu/web/2020/projects/2/commerce/)<br>
Demo video:  <https://youtu.be/pkFldBAgcPY>

#### Project 3 - Mail:
Front-end website for an email client that makes API calls to send and receive emails.<br>
Instructions [Here](https://cs50.harvard.edu/web/2020/projects/3/mail/)<br>
Demo video:  <https://youtu.be/XurnCD9iY8w>

#### Project 4 - Network:
Twitter-like social network website for making posts and following users.<br>
Instructions [Here](https://cs50.harvard.edu/web/2020/projects/0/search/)<br>
Demo video:  <https://youtu.be/Y4eNd6p5k48>

#### Project 5 - CAPSTONE (final project):
My final project. You'll find a readme document inside the Captsone folder that explains the projects and how to run it.<br>
Instructions [Here](https://cs50.harvard.edu/web/2020/projects/final/capstone/)<br> 
Demo video:  <https://youtu.be/_JwRIB4dgoU>


## Running each project

### Installation & How to run each project from 0 to 4 (the capstone projecct has its own readme file as it is a more complex project.)

In order to run a project, you need to install the dependencies found in the requirements.txt file in each folder for each project.

To start, open the folder containing the project you'd like to run.

Then you need to install Python. If not done already: Click [Here](https://www.python.org/downloads/) to do so.

After that, run the following command to create a Virtual Environment in the folder of the project you chose to run:

```bash
# Create a virtual environment
$ python3 -m venv
```

### Activate your environment
You’ll need to use different syntax for activating the virtual environment depending on which operating system and command shell you’re using.

On Unix or MacOS, using the bash shell: source /path/to/venv/bin/activate<br>
On Unix or MacOS, using the csh shell: source /path/to/venv/bin/activate.csh<br>
On Unix or MacOS, using the fish shell: source /path/to/venv/bin/activate.fish<br>
On Windows using the Command Prompt: path\to\venv\Scripts\activate.bat<br>
On Windows using PowerShell: path\to\venv\Scripts\Activate.ps1<br>

```bash
# After your environment has been activated, install the dependencies
$ pip install -r requirements.txt
```

```bash
# After that, you might need to make a migrations for the DB
$ python manage.py makemigrations
```
```bash
# Migrate
$ python manage.py migrate
```

```bash
# Finally, run the django project using 
$ python manage.py runserver
```


### More information about CS50 course and projects here:
More information on the whole course [Here]('https://cs50.harvard.edu/web/2020')
