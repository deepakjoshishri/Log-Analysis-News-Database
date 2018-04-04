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
Step 1. move into vagrant directory.<br>
Step 2. **vagrant up** command to run the vagrant on vm.<br>
Step 3. **vagrant ssh** to login into vm.<br>
Step 4. change directory to vagrant and make sure newsdata.sql file is present in it using **ls** command.<br>
Step 5. use command **psql -d news -f newsdata.sql** to load database.<br>
Step 6. use command **python Logs-udacity.py** or **python3 Logs-udacity.py** to run the program.<br>

### PSQL queries used To create the views

```sql
CREATE VIEW author_info AS
SELECT authors.name, articles.title, articles.slug
FROM articles, authors
WHERE articles.author = authors.id
ORDER BY authors.name;
```

```sql
CREATE VIEW path_view AS
SELECT path, COUNT(*) AS view
FROM log
GROUP BY path
ORDER BY path;
```

```sql
CREATE VIEW article_view AS
SELECT author_info.name, author_info.title, path_view.view
FROM author_info, path_view
WHERE path_view.path = CONCAT('/article/', author_info.slug)
ORDER BY author_info.name;
```

```sql
CREATE VIEW total_view AS
SELECT date(time), COUNT(*) AS views
FROM log 
GROUP BY date(time)
ORDER BY date(time);
```

```sql
CREATE VIEW error_view AS
SELECT date(time), COUNT(*) AS errors
FROM log WHERE status = '404 NOT FOUND' 
GROUP BY date(time) 
ORDER BY date(time);
```

```sql
CREATE VIEW error_rate AS
SELECT total_view.date, (100.0*error_view.errors/total_view.views) AS percentage
FROM total_view, error_view
WHERE total_view.date = error_view.date
ORDER BY total_view.date;
```

## Output should look like this:

**********************************************************************<br>
Question 1: Most popular articles are<br>
**********************************************************************<br>
+----------------------------------+--------+<br>
|              Title               | Views  |<br>
+----------------------------------+--------+<br>
| Candidate is jerk, alleges rival | 338647 |<br>
| Bears love berries, alleges bear | 253801 |<br>
| Bad things gone, say good people | 170098 |<br>
+----------------------------------+--------+<br>


**********************************************************************<br>
Question 2: Most popular authors are<br>
**********************************************************************<br>
+------------------------+--------+<br>
|         Title          | Views  |<br>
+------------------------+--------+<br>
|    Ursula La Multa     | 507594 |<br>
| Rudolf von Treppenwitz | 423457 |<br>
| Anonymous Contributor  | 170098 |<br>
|     Markoff Chaney     | 84557  |<br>
+------------------------+--------+<br>


**********************************************************************<br>
Question 3: Days with more than 1% errors are<br>
**********************************************************************<br>
+------------+--------------------+<br>
|    Date    |     Percentage     |<br>
+------------+--------------------+<br>
| 2016-07-17 | 2.2785265049415993 |<br>
+------------+--------------------+<br>
