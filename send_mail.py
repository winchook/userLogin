import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自winchoo的测试邮件', 'winchoo@163.com', '2032892453@qq.com'
    text_content = '欢迎访问，这里是winchoo的博客，专注于Python和Django技术的分享！'
    html_content = '<p>欢迎访问<a href="https://winchookgithub.wordpress.com/" target=blank>winchookgithub.wordpress.com</a>，这里是winchoo的博客和教程站点，专注于Python和Django技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()