import os
import time
from configparser import ConfigParser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from common import log

class email():
    def __init__(self,sender=None,recevier=None,smtp=None,user=None,password=None):
        self.file = os.path.abspath(os.path.join(os.getcwd(),'..','Businesses','test.xlsx'))
        file = os.path.abspath(os.path.join(os.getcwd(),'..','database','config'))
        config = ConfigParser()
        config.read(file)
        self.sender = config.get('email','sender')
        self.recevier = config.get('email','recevier')
        self.smtp = config.get('email','smtp')
        self.user = config.get('email','user')
        self.password = config.get('email','password')

    def send_email(self):
        today = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

        #发送附件
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = self.recevier
        msg['Subject'] = '软件测试情况'

        # 发送邮件正文内容，三个参数：第一个为文本内容，第二个 html 设置文本格式，第三个 utf-8 设置编码
        msg.attach(MIMEText('测试结果','plain','utf -8'))

        #将xlsx文件作为内容发送到对方的邮箱读取excel，rb形式读取，对于MIMEText()来说默认的编码形式是base64 ，没有设备会出现乱码
        fj = MIMEText(open(self.file,'rb').read(),'base64','utf -8')
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
            log.Log().info('发送成功')
            smtp.close()
        except Exception as e:
            log.Log().debug('发送失败'.format(e))


if __name__ == '__main__':
    test = email()
    test.send_email()

