from django.db import models

nicknames = ['brown_eyes', 'desert_rose', 'yor_infinity', 'tiger_lily', 'golden_hair', 'follow_me',
             'sweet_chocolate', 'brilliant_lady', 'moon_shine', 'gentle_rudeness', 'love_rainbow', 'peach_juice',
             'love_power', 'energy_of_love', 'beautiful_girl', 'sweetheart_baby', 'strawberry_sunset',
             'vanilla_sunshine', 'sugar_babe', 'raspberry_rum', 'wild_rose', 'angel_eyes', 'vintage_paris',
             'dreams_of_life', 'honey_bun', 'prairies_princess', 'just_the_two_of_us', 'love_may_hurt',
             'ny_took_my_heart', 'tears_of_passion', 'last_mistake']

class PrettyNick(models.Model):
    nickname = models.CharField('pretty nick', max_length=300, null=True)

    def save(self, *args, **kwargs):
        self.nickname = nicknames[0]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'DataUser_PrettyNick'






















































