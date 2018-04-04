# Log-Analysis-News-Database
A Project which generates some useful reports using sql statements on a new database. 

Project is done under the [Udacity Full Stack Nanodegree](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

Project aims at building a report on a stored database using python 2.x or python3.x
and postgresql Relational database system.

## Report Includes:
1. What are the most popular three articles of all time?
  Which articles have been accessed the most?
  Present this information as a sorted list with the most popular article at the top

2. Who are the most popular article authors of all time?
  That is, when you sum up all of the articles each author has written, which authors get the most page views?
  Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors?
  The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

### Installation:
1.Install Vagrant from here [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
2.Download or clone from github [fullstack-nandegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm)
3.newsdata.sql file in vagrant directory [fullstack-nandegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm) of helps us to load a database in our vm postgres.

### How to run:
Step 1. move into vagrant directory 
Step 2. **vagrant up** command to run the vagrant on vm
Step 3. **vagrant ssh** to login into vm
Step 4. change directory to vagrant and make sure newsdata.sql file is present in it using **ls** command.
Step 5. use command **psql -d news -f newsdata.sql** to load database
Step 6. use command **python log.py** or **python3 log.py** to run the program
