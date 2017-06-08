#-*-coding:utf-8-*-
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from config import *
import smtplib

def _format_addr(s):
    name, addr=parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr,unicode) else addr))

def send_email(from_addr, password, to_addr, smtp_server, title, connect):
    msg=MIMEText(connect, 'plain', 'utf-8')
    msg['From']=_format_addr(u'%s' % from_addr)
    msg['To']=_format_addr(u'%s' % to_addr)
    msg['Subject']=Header(title,'utf-8').encode()
    try:
        server=smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr,password)
        server.sendmail(from_addr,[to_addr],msg.as_string())
        server.quit()
        return True
    except Exception as e:
        return False


if __name__ == '__main__':
    from_addr = FROM_ADDR
    password = PASSWORD
    to_addr = TO_ADDR
    smtp_server = 'smtp.163.com'
    title = u'测试邮件'
    connect = u'这是一封测试邮件!'

    if send_email(from_addr, password, to_addr, smtp_server, title, connect):
        print 'sucess'
    else:
        print 'error'