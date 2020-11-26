from django.db import models

# Create your models here.
class Poll(models.Model):
    #投票主題文字，至多 200 字
    subject = models.CharField("主題投票", max_length=255)
    description =models.TextField("投票內容說明")
    # 投票建立日期，在建立時若未指定，則自動填入建立時的時間
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ")" + self.subject

class Option(models.Model):
    # 此選項屬於哪一個投票
    poll_id = models.IntegerField("所需投票主題編號")
    # 選項文字
    title = models.CharField("選項標題", max_length=200)
    # 此選項被投票數
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + ")" + self.subject

class Option(models.Model):
    poll_id = models.IntegerField('所屬投票主題')
    title = models.CharField('選樣標題', max_length = 200)
    count = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.id) + "+" +self.title +"@" +str(self.poll_id)