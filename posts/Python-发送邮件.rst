---
title: Python 发送邮件
date: 2019-08-13 12:43:42
tags:
  - python
categories: 记录
---

Python 发送邮件
===============

可以使用标准库模块 ``smtplib``, 但这个只是一个客户端,
仍然需要登录到服务器. 例如 Outlook, Gmail 等, 需要开启 POP3 或 IMAP
支持.


配置邮件服务器
--------------

以 Outlook 为例, 登录 Outlook 网页端, 参考
`官方说明 <https://support.office.com/zh-cn/article/Outlook-com-%E7%9A%84-POP%E3%80%81IMAP-%E5%92%8C-SMTP-%E8%AE%BE%E7%BD%AE-d088b986-291d-42b8-9564-9c414e2aa040>`__
进行操作.

在默认情况下, 已经启用了 IMAP 和 SMTP.

注意, 如果是发送邮件的话, 应当使用 SMTP, IMAP 是用于接收邮件的协议.

发送文本内容
------------

一下代码已验证可成功运行：

.. code:: python

   import smtplib
   from email.mime.text import MIMEText
   # in module zolook

   # Use in :meth:`Outlook.login`
   # read password from file
   PASSWORD_FROM_FILE = -1000
   # use getpass lib
   PASSWORD_FROM_PROMPT = -1001

   class Outlook:
       """Simple Outlook Client written by Python

       Exmaple
       =======

       >>> from zolook import Outlook
       >>> from email.mime.text import MIMEText
       >>> # Writing Email
       >>> email = MIMEText("test email from zolook", "plain", "utf-8")
       >>> email["Subject"] = "Testing"
       >>> email["From"] = "fromuser@outlook.com"
       >>> email["To"] = "target@outlook.com"
       >>> # Login
       >>> o = Outlook()
       >>> o.login("fromuser@outlook.com", Outlook.PASSWORD_FROM_PROMPT)
       >>> # input password in terminal
       >>> # Send
       >>> o.send(email, "target@outlook.com")
       """
       # basic configuration
       SMTP_SERVER = "smtp.office365.com"
       SMTP_PORT = 587
       # CRYPTION = "STARTTLS"

       def __init__(self):
           self.__username = None
           self.__password = None

       def login(self, username: str, password=PASSWORD_FROM_FILE, **kw):
           """login

           :param str username: Should be complete name with domain, such as ``someone@outlook.com``
           :param password: If use default value ``Outlook.PASSWORD_FROM_FILE``, should give additional keyword argument ``path``. If use ``Outlook.PASSWORD_FROM_PROMPT``, will use getpass.

           :param str path: optional. specify password file. if not suppose, default is ``./PASSWORD``
           """
           if password == PASSWORD_FROM_FILE:
               with open(kw.get("path", "PASSWORD"), "rt", encoding="utf-8") as file:
                   pw = file.read()
           elif password == PASSWORD_FROM_PROMPT:
               from getpass import getpass
               pw = getpass(f"password <{username}>: ")
           pw = pw.strip("\r\n")
           self.__password = pw
           self.__username = username

       def send(self, msg, to: str):
           """send a email

           :param msg: a Mail instance, can be MIMEText, MIMEMultipart and so on.
               the attributes ``From`` and ``To`` will be automatically insert.
           """
           s = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
           s.ehlo()
           s.starttls()
           s.ehlo()
           s.login(self.__username, self.__password)
           msg["From"] = self.__username
           msg["To"] = to
           mail = msg.as_string()
           s.sendmail(
               from_addr=self.__username,
               to_addrs=[to, ],
               msg=mail
           )
           s.quit()

但是 Outlook 会封禁新建的发送垃圾邮件的账户，我在进行测试的时候中招了。
返回 SMTP 554 错误码。听说国内 163， qq
等邮箱对此限制较为宽松，感兴趣者可以在这些邮箱上进行尝试。
