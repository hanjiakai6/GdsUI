import os
import configparser
#ini配置文件读取
current_path=os.path.dirname(__file__)
config_path=os.path.join(current_path,'../Config/config.ini')
class ConfigUntil():
    def __init__(self,path=config_path):
        self.cfg=configparser.ConfigParser()
        self.cfg.read(path,encoding='utf-8')

    @property
    def get_url(self):
        value=self.cfg.get('default','url')
        return value

    @property
    def get_driver_path(self):
        value=self.cfg.get('default','driver_path')
        return value

    @property
    def driver_name(self):
        value = self.cfg.get('default', 'driver_name')
        return value

    @property
    def time_out(self):
        value = self.cfg.get('default', 'time_out')
        return value

    @property
    def screent_shot_path(self):
        value = self.cfg.get('default', 'screent_shot_path')
        return value

    @property
    def user_name(self):
        value = self.cfg.get('default', 'user_name')
        return value

    @property
    def password(self):
        value = self.cfg.get('default', 'password')
        return value

    @property
    def impl_time(self):
        value = self.cfg.get('default', 'impl_time')
        return value

    @property
    def user_name_text(self):
        value = self.cfg.get('default', 'user_name_text')
        return value

    @property
    def log_level(self):
        value = int(self.cfg.get('default', 'log_level'))
        return value

    @property
    def testdate_path(self):
        value = self.cfg.get('default', 'testdate_path')
        return value

    @property
    def case_path(self):
        value = self.cfg.get('default', 'case_path')
        return value

    @property
    def report_path(self):
        value = self.cfg.get('default', 'report_path')
        return value

local_config=ConfigUntil()

if __name__ == '__main__':
    print(local_config.get_url)
    print(local_config.get_driver_path)
    print(local_config.driver_name)
    print(local_config.time_out)
    print(local_config.screent_shot_path)
    print(type(local_config.log_level))
    print(local_config.testdate_path)