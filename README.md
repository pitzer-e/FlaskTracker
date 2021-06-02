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
A standard user is able to register for an account that they will be able to log in to the application with. 
They are able to view their own data, and enter locations that they have visited themselves. They can't view others 
data, or enter data for others. They can also generate a report of the places that they have been, and what their 
chance of infection might be depending on the infection chance of the locations they visited.

#### System Administrator
The system administrator is the user which is built into the system for administration purposes. They are able
to change whether a standard user is infected or not, and can also alter the chance of infection for any of the given
locations.

#### Running the Application
The program can be run by navigating to the working directory and calling:

    /../FlaskTracker/python3 run.py

Or by using an IDE such as PyCharm and running the program using the Run 'FlaskTracker' button.

## Misc
This section is intended to be used as an area to communicate how major changes are handled within the framework of the
project. The sections included are intended to be used to help provide a more uniform approach to the documentation
that can be found in commit uploads and ReadMe edits. These guidelines are suggested to provide a uniform approach 
to project contributions.

#### Formatting
* The commit updates follow the following format:  <i>year-month-day, summary of update
</i>
  
#### Suggested tools
* <https://sqlitebrowser.org>
* <https://www.jetbrains.com/pycharm/>