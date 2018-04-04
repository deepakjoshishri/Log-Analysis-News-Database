'''!/usr/bin/env python3
import prettytable.py which is used for desgining table
import os for clearing screen before execution'''
import prettytable
import psycopg2
import os


def main():
    os.system('clear')
    # Connect to an existing database
    conn = psycopg2.connect("dbname=news")

    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Question 1
    sql_popular_articles = """
      SELECT article_view.title, article_view.view
      FROM article_view
      ORDER BY article_view.view DESC
      LIMIT 3;
    """
    cur.execute(sql_popular_articles)
    print("*" * 70)
    print("Question 1: Most popular articles are")
    print("*" * 70)
    printTable(cur)
    print("\n")

    # Question 2
    sql_popular_authors = """
    SELECT article_view.name, SUM(article_view.view) AS author_view
    FROM article_view
    GROUP BY article_view.name
    ORDER BY author_view DESC;
    """
    cur.execute(sql_popular_authors)
    print("*" * 70)
    print("Question 2: Most popular authors are")
    print("*" * 70)
    printTable(cur)
    print("\n")

    # Question 3
    sql_more_than_one_percent_errors = """
    SELECT *
    FROM error_rate
    WHERE error_rate.percentage > 1
    ORDER BY error_rate.percentage DESC;
    """
    cur.execute(sql_more_than_one_percent_errors)
    x = prettytable.PrettyTable(["Date", "Percentage"])
    print("*" * 70)
    print("Question 3: Days with more than 1% errors are")
    print("*" * 70)
    for (date, percentage) in cur.fetchall():
        x.add_row([date, percentage])
    print(x)
    print("\n")

    # Close communication with the database
    cur.close()
    conn.close()
''' prettytable.PrettyTable(["header name", "header name"])
    x.add_row([data, data]) -> x.add_row([title, view]) '''


def printTable(cur):
    x = prettytable.PrettyTable(["Title", "Views"])
    for (title, view) in cur.fetchall():
        x.add_row([title, view])
    print(x)

if __name__ == "__main__":
    main()
