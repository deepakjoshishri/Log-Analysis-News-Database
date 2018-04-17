# !/usr/bin/env python3

# import prettytable.py which is used for desgining table
# import os for clearing screen before execution

import prettytable
import psycopg2
import os


def main():
    os.system('clear')
    # Connect to an existing database
    conn = psycopg2.connect("news")

    # Open a cursor to perform database operations
    current = conn.cursor()
    most_popular_articles_3(current)
    most_popular_authors(current)
    more_than_one_percent_errors(current)

    # Close connection with the database
    current.close()
    conn.close()


def most_popular_articles_3(current):
    # 1. What are the most popular three articles of all time?
    most_popular_articles_3 = """
      select title, view
      from view_article
      order by view DESC
      LIMIT 3;
    """
    current.execute(most_popular_articles_3)
    print("*" * 70)
    print("Question 1: Most popular articles are")
    print("*" * 70)
    printTable(current)
    print("\n")


def most_popular_authors(current):
    # 2. Who are the most popular article authors of all time?
    most_popular_authors = """
    select A.name, SUM(A.view) AS AU
    from view_article AS A
    GROUP by A.name
    order by AU DESC;
    """
    current.execute(most_popular_authors)
    print("*" * 70)
    print("Question 2: Most popular authors are")
    print("*" * 70)
    printTable(current)
    print("\n")


def more_than_one_percent_errors(current):
    # 3. On which days did more than 1% of requests lead to errors?
    more_than_one_percent_errors = """
    select *
    from error_rate AS E
    where E.percentage > 1
    order by E.percentage DESC;
    """
    current.execute(more_than_one_percent_errors)
    x = prettytable.PrettyTable(["Date", "Percentage"])
    print("*" * 70)
    print("Question 3: Days with more than 1% errors are")
    print("*" * 70)
    for (date, percentage) in cur.fetchall():
        x.add_row([date, percentage])
    print(x)
    print("\n")


def printTable(current):
    # prettytable.PrettyTable(["header name", "header name"])
    # x.add_row([data, data]) -> x.add_row([title, view])
    x = prettytable.PrettyTable(["Title", "views"])
    for (title, view) in current.fetchall():
        x.add_row([title, view])
    print(x)


if __name__ == "__main__":
    main()
