import requests
from twilio.rest import Client
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def send_sms():
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='666 oracle status is false',
        from_ = '',
        to = ''
    )

    print(message.sid)


url = ""

mark = 0

def job():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    r = requests.get(url)
    data = r.json()
    is_active = data['result']['is_active']
    print(now)
    print(is_active)

    if not is_active:
        mark += 1

        if mark < 3:
            send_sms()

sched = BlockingScheduler()
sched.add_job(job, 'interval', seconds=30)
sched.start()
