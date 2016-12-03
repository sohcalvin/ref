from apscheduler.schedulers.blocking import BlockingScheduler
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Start --===================')

def printIt() :
    logger.info('Hellow --===================')
    print("Hello")

if __name__ == '__main__':
    printIt()
    scheduler = BlockingScheduler()
    scheduler.add_job(printIt, 'cron', minute='0,5,10,15,20,25,30,35,40,45,50,55',coalesce=True)
    scheduler.start()


