# !/usr/bin/env python3

'''import prettytable.py which is used for desgining table
import os for clearing screen before execution'''
import prettytable
import psycopg2
import os


def main():
    os.system('clear')
    # Connect to an existing database
    conn = psycopg2.connect("news")

    # Open a cursor to perform database operations
    current = conn.cursor()
    # 1. What are the most popular three articles of all time?
    most_popular_articles_3 = """
      SELECT title, view
      FROM article_view
      ORDER BY view DESC
      LIMIT 3;
    """
    current.execute(most_popular_articles_3)
    print("*" * 70)
    print("Question 1: Most popular articles are")
    print("*" * 70)
    printTable(current)
    print("\n")

    # 2. Who are the most popular article authors of all time?
    most_popular_authors = """
    SELECT A.name, SUM(A.view) AS AU
    FROM article_view AS A
    GROUP BY A.name
    ORDER BY AU DESC;
    """
    current.execute(most_popular_authors)
    print("*" * 70)
    print("Question 2: Most popular authors are")
    print("*" * 70)
    printTable(current)
    print("\n")

    # 3. On which days did more than 1% of requests lead to errors?
    more_than_one_percent_errors = """
    SELECT *
    FROM error_rate AS E
    WHERE E.percentage > 1
    ORDER BY E.percentage DESC;
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

    # Close connection with the database
    current.close()
    conn.close()
''' prettytable.PrettyTable(["header name", "header name"])
    x.add_row([data, data]) -> x.add_row([title, view]) '''


def printTable(current):
    x = prettytable.PrettyTable(["Title", "Views"])
    for (title, view) in current.fetchall():
        x.add_row([title, view])
    print(x)

if __name__ == "__main__":
    main()
