import json
import mysql.connector
import csv
from datetime import datetime, timedelta

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="198237645",
  database="drugsDB"
)
mycursor = mydb.cursor()

data = []
for i in range(1, 25):
    with open(f'UnapprovedDrug/data_Cal/data{i}.json') as f:
                events = json.load(f)

    result = [{"company": event["summary"].split()[1 ], "date": event["start"]["date"]} for event in events if event["organizer"]["displayName"] == "PDUFA"]
    data= data + result

# for com in data:
#     print(com["company"])
notPass = []
# data = [{'company': 'CorMedix', 'date': '2023-11-17'}]
for com in data:
    # get all the application numbers by company name
    appNoSql = f'select * from Applications WHERE SponsorName like  "{com["company"]}%"'
    mycursor.execute(appNoSql)
    appNos = [result[0] for result in mycursor.fetchall()]

    # if no application numbers found, add to the notPass list
    if len(appNos) == 0:
        notPass.append(com)
        continue
    
    # convert the date and application numbers to the right format
    appNos = ', '.join(map(str, appNos))
    # original_date = com["date"]
    original_date = datetime.strptime(com["date"], '%Y-%m-%d')
    date_5_days_before = (original_date - timedelta(days=5)).strftime('%Y-%m-%d')
    date_10_days_later = (original_date + timedelta(days=10)).strftime('%Y-%m-%d')
    # year, month, day = original_date.split('-')
    # day = (int(day)//10)
    # new_date = f"{year}-{month}-{str(day)}%"
    # new_date_2 = f"{year}-{month}-{str(day+1)}%"
    # get the application docs by date and application numbers
    # checkSql = f'SELECT ApplNo, SubmissionType, ApplicationDocsDate, ApplicationDocsURL, ApplicationDocsTypeID FROM application_docs WHERE (ApplicationDocsDate LIKE "{new_date} 00:00:00" OR ApplicationDocsDate LIKE "{new_date_2} 00:00:00") AND ApplNo IN ({appNos})'
    checkSql = f'SELECT ApplNo, SubmissionType, ApplicationDocsDate, ApplicationDocsURL, ApplicationDocsTypeID FROM application_docs WHERE (ApplicationDocsDate >= "{date_5_days_before} 00:00:00" AND ApplicationDocsDate <= "{date_10_days_later} 00:00:00") AND ApplNo IN ({appNos})'
    # checkSql = f'SELECT ApplNo, SubmissionType, ApplicationDocsDate, ApplicationDocsURL, ApplicationDocsTypeID FROM application_docs WHERE ApplicationDocsDate LIKE "{new_date} 00:00:00" AND ApplNo IN ({appNos})'
    mycursor.execute(checkSql)
    results = mycursor.fetchall()

    # if no docs found, add to the notPass list
    if len(results) == 0:
        notPass.append(com)
        continue

print(notPass)
print(len(notPass))


csv_file = 'UnapprovedDrug/output/unapprovedDrug.csv'

# Specify the fieldnames (column names) based on the dictionary keys
fieldnames = ['company', 'date']

# Write the data to the CSV file
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header
    writer.writeheader()
    
    # Write the data
    writer.writerows(notPass)

print(f'Data has been written to {csv_file}')


# appNoSql = f'select * from Applications WHERE SponsorName like  "cormedix%"'
# mycursor.execute(appNoSql)
# appNos = [result[0] for result in mycursor.fetchall()]
# print(appNos)
# appNos = ', '.join(map(str, appNos))
# checkSql = f'SELECT ApplNo, SubmissionType, ApplicationDocsDate, ApplicationDocsURL, ApplicationDocsTypeID FROM application_docs WHERE ApplicationDocsDate LIKE "2023-11-1% 00:00:00" AND ApplNo IN ({appNos})'
# mycursor.execute(checkSql)
# results = mycursor.fetchall()
# print(results)