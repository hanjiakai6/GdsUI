import logging,os,time
from PO设计.Common.config_untils import local_config
now_time=time.strftime('%Y-%m-%d')
current_path=os.path.dirname(__file__)
log_path=os.path.join(current_path,'../Logs/all_logs_{}.log'.format(now_time))
class Logging():
    def __init__(self,log_path=log_path):
        self.log_path=log_path
        self.logger=logging.getLogger()
        self.logger.setLevel(local_config.log_level)

        self.fh=logging.FileHandler(log_path,encoding='utf-8')
        self.fh.setLevel(local_config.log_level)
        self.ch=logging.StreamHandler()
        self.ch.setLevel(local_config.log_level)
        formater=logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        self.fh.setFormatter(formater)
        self.ch.setFormatter(formater)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)
        self.fh.close()
        self.ch.close()
    def info(self,a):
        self.logger.info(a)
    def error(self,a):
        self.logger.error(a)
#logging实例对象
logger=Logging()

if __name__ == '__main__':
    logger.info('123')
    logger.fh.setLevel(40)
    logger.info('888')
