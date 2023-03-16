from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models import Avg
from django.utils import timezone
from django.utils.text import slugify


class Genre(models.Model):
    """Жанры произведений. Одно произведение может быть привязано к нескольким жанрам."""
    name = models.CharField(
        max_length=256,
        verbose_name="Имя жанра",
    )
    slug = models.SlugField(
        max_length=50,
        verbose_name="Слаг жанра",
        unique=True,
    )

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(models.Model):
    """Категории (типы) произведений («Фильмы», «Книги», «Музыка»). Одно произведение может быть привязано
    только к одной категории"""
    name = models.CharField(
        max_length=256,
        verbose_name="Имя категории",
    )
    slug = models.SlugField(
        max_length=50,
        verbose_name="Слаг категории",
        unique=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Review(models.Model):
    # todo: раскомментировать и заменить IntegerField после объявления моделей юзера и Title
    author = models.IntegerField()  # ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    title = models.IntegerField()  # ForeignKey(Title, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    score = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(10)]
                                )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    # todo: раскомментировать и заменить IntegerField после объявления модели юзера
    author = models.IntegerField()  # ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name='comments'
                               )
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text


class Title(models.Model):
    """ Произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
    Наполнение доступно только администратору"""
    name = models.CharField(
        max_length=256,
        verbose_name="Произведение",
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
        blank=True,
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
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.name}, {self.category}, {self.genre}, {self.year}'

    # todo:def get_rating(self):
    #     rating = self.reviews.aggregate(models.Avg('score'))['score__avg']
    #     return int(rating)
