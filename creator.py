import sys
import time
import mysql.connector

# Settings

# Database Information's
db_host = ""
db_user = ""
db_password = ""
database = ""

# count containers equals to how much ips you have and DON'T TOUCH TO COUNT!
count_container = 254
count = 2

try:
    while True:
        # if count not equals to count of containers (count_container) create new one until its equals
        if count != int(count_container):
            mydb = mysql.connector.connect(
                host=f"{db_host}",
                user=f"{db_user}",
                password=f"{db_password}",
                database=f"{database}"
            )

            try:
                mycursor = mydb.cursor()
            except Exception as db_error:
                print(f"MySQL Connection Error: {db_error}")

            sql = "SELECT * FROM honey_accounts"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
        for honey_account in myresult:
            subnet = '{}.{}.{}'.format(*__import__('random').sample(range(0, 255), 4))
            print(f"docker network create main{count} --driver bridge --subnet {subnet}.0/24 ; iptables -t nat -I POSTROUTING -s {subnet}.0/24 -j NETMAP --to 5.105.24.0/24 ; docker run -d --network main{count} --ip {subnet}.{count} --name HoneyGain_{subnet}.{count} honeygain/honeygain -tou-accept -email {honey_account[0]} -pass {honey_account[1]} -device {subnet}.{count}")

            subnet2 = '{}.{}.{}'.format(*__import__('random').sample(range(0, 255), 4))
            print(f"docker network create main{count+1} --driver bridge --subnet {subnet2}.0/24 ; iptables -t nat -I POSTROUTING -s {subnet2}.0/24 -j NETMAP --to 5.105.24.0/24 ; docker run -d --network main{count+1} --ip {subnet2}.{count+1} --name HoneyGain_{subnet2}.{count+1} honeygain/honeygain -tou-accept -email {honey_account[0]} -pass {honey_account[1]} -device {subnet2}.{count+1}")

            subnet3 = '{}.{}.{}'.format(*__import__('random').sample(range(0, 255), 4))
            print(f"docker network create main{count+2} --driver bridge --subnet {subnet3}.0/24 ; iptables -t nat -I POSTROUTING -s {subnet3}.0/24 -j NETMAP --to 5.105.24.0/24 ; docker run -d --network main{count+2} --ip {subnet3}.{count+2} --name HoneyGain_{subnet3}.{count+2} honeygain/honeygain -tou-accept -email {honey_account[0]} -pass {honey_account[1]} -device {subnet3}.{count+2}")

            subnet4 = '{}.{}.{}'.format(*__import__('random').sample(range(0, 255), 4))
            print(f"docker network create main{count+3} --driver bridge --subnet {subnet4}.0/24 ; iptables -t nat -I POSTROUTING -s {subnet4}.0/24 -j NETMAP --to 5.105.24.0/24 ; docker run -d --network main{count+3} --ip {subnet4}.{count+3} --name HoneyGain_{subnet4}.{count+3} honeygain/honeygain -tou-accept -email {honey_account[0]} -pass {honey_account[1]} -device {subnet4}.{count+3}")

            subnet5 = '{}.{}.{}'.format(*__import__('random').sample(range(0, 255), 4))
            print(f"docker network create main{count+4} --driver bridge --subnet {subnet5}.0/24 ; iptables -t nat -I POSTROUTING -s {subnet5}.0/24 -j NETMAP --to 5.105.24.0/24 ; docker run -d --network main{count+4} --ip {subnet5}.{count+4} --name HoneyGain_{subnet5}.{count+4} honeygain/honeygain -tou-accept -email {honey_account[0]} -pass {honey_account[1]} -device {subnet5}.{count+4}")
            count = count + 5
            # a little time sleep for don't overheat machine
            time.sleep(0.5)

            # Add account to in use accounts table
            sql = f"INSERT INTO in_use_accounts SELECT * FROM honey_accounts WHERE email = '{honey_account[0]}'"
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")

            # Delete account from honey accounts table
            sql = f"DELETE FROM honey_accounts WHERE email = '{honey_account[0]}'"
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount, "record(s) deleted")

        else:
            # Print that says work done (you will not see that because we will use it in background) and exit script (don't know really we need that)
            print("Work Done...")
            sys.exit()

except Exception as main_error:
    # That's just exception error output
    print(f"Main Error: {main_error}")
