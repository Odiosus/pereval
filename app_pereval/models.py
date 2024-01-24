from django.db import models

from .choices import LEVELS, STATUS


class AppUser(models.Model):
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    name = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=30, blank=True, default=None, verbose_name='Отчество')

    def __str__(self):
        return f'{self.email}'


class Coords(models.Model):
    latitude = models.FloatField(max_length=8, verbose_name='Широта')
    longitude = models.FloatField(max_length=8, verbose_name='Долгота')
    height = models.IntegerField(max_length=4, verbose_name='Высота')

    def __str__(self):
        return f'широта: {self.latitude}, долгота: {self.longitude}, высота: {self.height}'


class Level(models.Model):
    winter = models.CharField(max_length=2, choices=LEVELS, default='', verbose_name='Категория трудности: ЗИМА')
    summer = models.CharField(max_length=2, choices=LEVELS, default='', verbose_name='Категория трудности: ЛЕТО')
    autumn = models.CharField(max_length=2, choices=LEVELS, default='', verbose_name='Категория трудности: ОСЕНЬ')
    spring = models.CharField(max_length=2, choices=LEVELS, default='', verbose_name='Категория трудности: ВЕСНА')

    def __str__(self):
        return f'зима: {self.winter}, лето: {self.summer}, осень: {self.autumn}, весна: {self.spring}'


class Pereval(models.Model):
    status = models.CharField(max_length=100, choices=STATUS, default='new', verbose_name='Статус модерации')
    beauty_title = models.CharField(max_length=250, verbose_name='Тип локации')
    title = models.CharField(max_length=250, verbose_name='Название локации')
    other_titles = models.CharField(max_length=250, blank=True, default=None, verbose_name='Описание локации')
    connect = models.CharField(max_length=250, verbose_name='Какие локации соединяет?')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    coord_id = models.OneToOneField(Coords, on_delete=models.CASCADE, verbose_name='Координаты')
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    level = models.OneToOneField(Level, on_delete=models.PROTECT, verbose_name='Категория трудности')

    def __str__(self):
        return f'{self.title}'


def get_path_upload_images(instance, file):
    return f'images/pereval-{instance.pereval.id}/{file}'


class Images(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    images = models.ImageField(upload_to=get_path_upload_images, default=None, blank=True, null=True,
                               verbose_name="Фото")
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images', verbose_name='Локация')

    def __str__(self):
        return f'{self.pereval}'
