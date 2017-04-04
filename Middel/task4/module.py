import csv
import re
import sqlite3

def write_csv(email, count, date):
    with open('test.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((email, count, date))

def email(data):
    all_pattern = re.compile('^From ([\w\.]+@[\w\.]+) [A-Z][a-z]{2}\s([A-Z][a-z]{2})', re.M)
    emails_pattern = re.compile('^From ([\w\.]+@[\w\.]+) [A-Z][a-z]{2}\s[A-Z][a-z]{2}', re.M)
    data_all = all_pattern.findall(data)
    emails = emails_pattern.findall(data)
    lats_date_all = {email:date for email,date in data_all}
    write_csv('email', 'count', 'date')

    for i in set(emails):
        print i, emails.count(i), lats_date_all[i]
        write_csv(i, emails.count(i), lats_date_all[i])

if __name__ == "__main__":
    data = open('mbox.txt', 'rU').read()
    print email(data)


