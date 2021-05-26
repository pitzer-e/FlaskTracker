# FlaskTracker
FlaskTracker is a simple web-application program using the Flask framework.  This application can be used to create a 
user, who is able to view locations that are available in the La Grande, OR area. A user may select one of these 
locations as a location that they have recently visited, which will add their data to the app. From there, the user may 
choose to generate a report of their data from a separate web page. This report will contain the percent chance that a 
user might be infected, based on other users, who may have been infected which also (previously) visited the
same location.  If the user is identified as having a high or assured percentage of infection, they may choose to 
generate a path that shows where they were most likely to have become infected.


## Developers
* Ethan Pitzer, pitzere@eou.edu, pitzer-e
* Dan Hughes, dthughes@eou.edu, DanTheFisherman
* Noah Chaney, njchaney@eou.edu, njchaney
* Steve Wilkins, swilkins@eou.edu, imminent-darkness

## Usage
There are two primary users in mind with this application:
* The standard user
* The system administrator

#### Standard User
The standard user should be able to register for an account that they will be able to log in to the application with
in order to enter data for themselves. They should only be able to view their own data, and enter locations that they
have visited themselves. No viewing of others data, or entering of data for others. The standard can also generate a
report of the places that they have been, and what their chance might be depending on the infection chance of the
locations that they have visited were.

#### System Administrator
The system administrator is the user which is built into the system for administration purposes. The admin user is able
to change whether a standard user is infected or not, and can also change the chance of infection for any of the given
locations.

## Updates
This section intends to provide the reader with a more detailed
explanation of the underlying updates which were included in a 
given update. Throughout the development process, updated code
will be pushed to our Git repository, which will include a small
description of the update which was included.

#### Notice
* As of 2021-05-25, it is recommended that updates adhere the following format:  <i>year-month-day, summary of update
</i><br>
* It is recommended for developers to tac their name at the end of an update within this Readme to better track
changelogs through the document should further inquiry into the update provided be required

### 2021-05-18, Initial Git Commit
The initial commit saw the creation of the Git repository. The FlaskTracker project includes all necessary libraries and
packages for the application to function.  The initial HTML files were created for the project using BootStrap 
templates, and a simple .py file was created for app definition and imports.<br>
-pitzer-e

### 2021-05-19, New HTML & Documentation
The updated code pushed to Git VCS on 2021-05-19 included a new HTML page titled 'report.html' which is intended to 
serve as the web-page responsible for hosting and serving report generation functionality. Additional documentation was 
added to better document code changes going forward.<br>
-pitzer-e

### 2021-05-24, Page Naming & Small Updates
This update was minor. The 'location.html' page was changed to be renamed to 'data.html', along with renaming the
appropriate areas throughout the project document.<br><br>It is important to note that there was one large change to 
the working Git file. While nothing has changed regarding filename, a new repository was created which has a new 
build-hierarchy.<br><br> Because of this, an updated link to the new repository was sent out to teammates on 2021-05-24 
to ensure continued and updated access to the working project repository. The rebuild is intended to allow for better 
linked Git updates to the remote-Git repository location via commit/push actions through local IDE's (i.e, PyCharm).<br> 
-pitzer-e

### 2021-05-25, Updated Libraries and SQLAlchemy
Multiple updates were pushed to the repository this date, and are recorded below by issue, followed by a timestamp of 
when the change was committed and a tac of the user making the change.
#### Issue #1 (0800)
This was a large update for the FlaskTracker project. The virtual environment directory was updated to include the 
flask-sqlalchemy library, so that the SQLAlchemy object could be called during the creation of the SQLite3
database. Additionally, in order to accommodate this, the virtual environment needed to reflect changes to the 
underlying python libraries.  Python 2.7 was retired in January 2021, and as such, no longer included updates to the 
flask sqlalchemy packages.  Because of this, pip3 (Python3 package handler) was used to re-package the 
underlying python dependencies so that the latest(currently 3.9) Python development environment can be used.<br>
-pitzer-e


#### Issue #2 (1000)
Following the Python update, the latest flask-sqlalchemy libraries were packaged and included into this update of 
FlaskTracker.  A new HTML5 file was created 'base.html', which is to be used as the extended template for other HTML 
pages to include. This helps create a more modular environment, and allows for cleaner web-side development. Jinja2 
templating has begun inclusion at this point of development, and was used to provide url linking to the var_bar tables 
for maneuvering throughout the website.<br>
-pitzer-e

#### Issue #3 (1600)
SQLite3 database 'tracker' was created for the FlaskTracker project. The initial User table was created to host user
data for the application.<br>
-pitzer-e

#### Issue #3 (1700)
A fourth HTML page was created 'admin.html'. This page is to prototype the concept of hosting an Admin page for the 
system administrator to be able to access. From here, the Administrator will be able to view all users of the page,
and change their infection status.
* Change user infection status
* Change location infection percentage chance

Readme documentation and formatting was also changed to provide a more uniform context.<br>
-pitzer-e