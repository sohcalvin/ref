import time, os
def printIt(text="Ho Ho Ho") :
    print(text)


def setupInterval() :
    from apscheduler.schedulers.background import BackgroundScheduler


    scheduler = BackgroundScheduler()
    # scheduler.add_job(printIt,"interval", seconds=3, coalesce=True )
    scheduler.add_cron_job(printIt, day_of_week='mon-fri', hour=5, minute=30)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:  time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        sched.shutdown()

    return scheduler

def setupCron() :
    from apscheduler.schedulers.blocking import BlockingScheduler
    scheduler = BlockingScheduler()
    #sched.add_job(printIt, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
    print("add1")
    scheduler.add_job(printIt, 'cron',['hello1'], hour=14, minute=00,coalesce=True)
    print("add1 fin")
    print("add2")
    scheduler.add_job(printIt, 'cron', ['hello2'], hour = 14, minute = 00, coalesce = True)
    print("add2 fin")
    scheduler.start()
    print("started")
    return scheduler

sched = setupCron()
print("Finished ...")


