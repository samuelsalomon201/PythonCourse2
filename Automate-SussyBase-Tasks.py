import psycopg2

try:
    connection = psycopg2.connect(database="staff", user="mihai", password="python", host="127.0.0.1", port="5432")

except psycopg2.Error as err:
    print("BUNER ALERT BUNER ALERT")

else:
    print("No Buners Detected")