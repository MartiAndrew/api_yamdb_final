from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

from user.models import User


class Genre(models.Model):
    """Жанры произведений.
    Одно произведение может быть привязано к нескольким жанрам."""
    name = models.CharField(
        max_length=256,
        verbose_name="Имя жанра",
    )
    slug = models.SlugField(
        max_length=50,
        verbose_name="Слаг жанра",
        db_index=True,
        unique=True,
    )

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Category(models.Model):
    """Категории (типы) произведений («Фильмы», «Книги», «Музыка»).
    Одно произведение может быть привязано только к одной категории"""
    name = models.CharField(
        max_length=256,
        verbose_name="Имя категории",
    )
    slug = models.SlugField(
        max_length=50,
        verbose_name="Слаг категории",
        db_index=True,
        unique=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Title(models.Model):
    """ Произведения, к которым пишут отзывы
    (определённый фильм, книга или песенка).
    Наполнение доступно только администратору"""
    name = models.CharField(
        max_length=256,
        verbose_name="Произведение",
        db_index=True,
    )
    description = models.TextField(
        max_length=256,
        verbose_name="Описание",
        null=True,
        blank=True,
    )
    year = models.IntegerField(
        verbose_name="Год выпуска",
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name="titles",
        verbose_name="Категория",
        null=True,
    )

    genre = models.ManyToManyField(
        Genre, related_name="titles",
        verbose_name="Жанр",
    )

    def clean(self):
        current_year = timezone.now().year
        if self.year < 1800 or self.year > current_year:
            raise ValidationError('Год должен быть между 1800 и текущим')

    class Meta:
        verbose_name = "Произведение"
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return f'{self.name}, {self.category}, {self.genre}, {self.year}'


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='reviews')
    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              related_name='reviews')
    text = models.TextField()
    score = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(10)])
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)
        unique_together = ('author', 'title')

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments')
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name='comments')
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text
