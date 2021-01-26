import os
import time
from configparser import ConfigParser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from common.log import Log

from data.Get_data import getdata

class email():
    def __init__(self,sender=None,recevier=None,smtp=None,user=None,password=None):
        self.file = os.path.abspath(os.path.join(os.getcwd(),'..','Businesses','test.xlsx'))
        file = os.path.abspath(os.path.join(os.getcwd(),'..','database','config'))
        self.rep = os.path.abspath(os.path.join(os.getcwd(),'..','report'))
        config = ConfigParser()
        config.read(file)
        self.sender = config.get('email','sender')
        self.recevier = config.get('email','recevier')
        self.smtp = config.get('email','smtp')
        self.user = config.get('email','user')
        self.password = config.get('email','password')

    #获取最新测试报告
    def get_report(self):
        dir_rep = os.listdir(self.rep)
        dict.sort()
        new_rep = dir_rep[-1]
        return new_rep

    def send_email(self):
        new_report = self.get_report()
        today = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

        #发送附件
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = self.recevier
        msg['Subject'] = '软件测试情况'

        # 发送邮件正文内容，三个参数：第一个为文本内容，第二个 html 设置文本格式，第三个 utf-8 设置编码
        msg.attach(MIMEText('测试结果','plain','utf -8'))

        #将xlsx文件作为内容发送到对方的邮箱读取excel，rb形式读取，对于MIMEText()来说默认的编码形式是base64 ，没有设备会出现乱码
        fj = MIMEText(open(new_report,'rb').read(),'base64','utf -8')
        fj["Content-Type"] = 'application/octet-stream'
        fj["Content-Disposition"] = 'attachment; filename="TestResult.xlsx"'
        msg.attach(fj)

        try:
            #发送者smtp服务器
            smtp = smtplib.SMTP_SSL()
            smtp.connect(self.smtp,'465')
            #发送者邮箱账号和授权码
            smtp.login(self.user,self.password)
            #发件人邮箱账号、收件人邮箱账号、发送邮件
            smtp.sendmail(self.sender,self.recevier,msg.as_string())
            Log().info('发送成功')
            smtp.close()
        except Exception as e:
            Log.debug('发送邮件失败')
            raise



if __name__ == '__main__':
    # test = email()
    # test.send_email()

    email().test()

