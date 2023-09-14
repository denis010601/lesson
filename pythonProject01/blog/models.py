from django.db import models


class Article(models.Model):
    title = models.CharField('Заголовок',max_length=50)     # Строка с огр знаками
    desc = models.TextField('Описание')      # Строка с огр знаками
    image = models.ImageField('Изображение',upload_to='blog/image/')       # Строка под Изображение
    date = models.DateField('Дата')        # Дата
    url = models.URLField('Доп.источник', blank=True)        # Ссылка

    def __str__(self):
        return f"{self.title} | {self.date}"

