import logging,time
from 线性设计.Public.public_Tool import Pub
class Logging():
    def __init__(self):
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.INFO)
        now_time=time.strftime('%Y-%m-%d')
        log_path=Pub.file_path('../Log/logs_{}.log'.format(now_time))
        fh=logging.FileHandler(log_path)
        fh.setLevel(logging.INFO)
        formater=logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        fh.setFormatter(formater)
        self.logger.addHandler(fh)
    def info(self,a):
        self.logger.info(a)
logger=Logging()

if __name__ == '__main__':
    now_time = time.strftime('%Y-%m-%d %H:%M:%S')
    print(now_time)
    logger.info('123')
