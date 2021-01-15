import logging
import time,os,datetime
from logging.handlers import TimedRotatingFileHandler

class Log:
    def __init__(self):
        #返回log文件夹路径
        self.log_path = os.path.abspath(os.path.join(os.getcwd(),'..','log'))
        today = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        #log日志命名
        self.logname = os.path.join(self.log_path,(today+'.log'))

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #日志输入格式
        self.formatter = logging.Formatter('[%(asctime)s]-%(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s')

    def outlog(self):
        # 文件夹列表
        dirfile = os.listdir(self.log_path)
        #获取当前时间
        now = datetime.datetime.now()
        #获取前5天
        movetime = datetime.timedelta(days=-5)
        re_date = (now+movetime)
        #转换时间戳
        re_date_unix = time.mktime(re_date.timetuple())

        try:
            for file in dirfile:
                #根据文件最后修改时间
                file_list = sorted(dirfile,key=lambda  x:os.path.getatime(os.path.join(self.log_path,x)))
                for f in file_list:
                    file_path2 = os.path.join(self.log_path,f)
                    #判断是否有文件
                    if os.path.isfile(file_path2):
                        # 删除文件时间小于等于5天
                        if os.path.getatime(file_path2) <= re_date_unix:
                            os.remove(file_path2)
                    # 限制日志数量为5
                    if len(file_list) > 5:
                        file_list = file_list[0:-5]
                        print(file_list)
                        for f in file_list:
                            file_path2 = os.path.join(self.log_path,f)
                            os.remove(file_path2)
        except Exception as e:
            str(e)


    def console(self,level,message):
        # 创建一个FileHandler，用于写到本地,使用RotatingFileHandler类，滚动备份日志
        fh = TimedRotatingFileHandler(filename=self.logname,encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        #判断日志级别
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'error':
            self.logger.error(message)

        #避免日志输出重复问题
        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)
        #关闭文件
        fh.close()

    def info(self,message):
        self.console('info',message)
    def debug(self,message):
        self.console('debug',message)
    def error(self,message):
        self.console('error',message)

if __name__ == '__main__':
    log = Log()
    log.debug('...kaishi')
    log.info('..dfudu ')
    log.error('...haha')
    log.outlog()