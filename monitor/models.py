from django.db import models


class Source(models.Model):
    VKONTAKTE = 'VK'
    INSTAGRAM = 'IN'
    TWITTER = 'TW'

    TYPE_SOCIAL = [
        (VKONTAKTE, 'Vkontakte'),
        (INSTAGRAM, 'Instagram'),
        (TWITTER, 'Twitter'),
    ]
    name = models.CharField('Название', max_length=250, blank=True, null=True, default='')
    link = models.TextField('Ссылка', null=False)
    internal_id = models.CharField('Внутренний ID', max_length=50, blank=True, null=True, default='')
    avatar = models.TextField('Аватар', blank=True, null=False)
    type_social = models.CharField('Социальная сеть', max_length=2, choices=TYPE_SOCIAL, null=False)

    def __str__(self):
        return f'{self.name} - {self.link}'

    def ordered_stats(self):
        return self.stat_set.order_by('-updated_at')

    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'
        ordering = ['-id', ]


class Stat(models.Model):
    count_subscribers = models.IntegerField('Подписчики', null=False, default=0)
    updated_at = models.DateTimeField('Обновлено', null=False)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'{self.source.name}({self.count_subscribers}, {self.updated_at})'

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'
