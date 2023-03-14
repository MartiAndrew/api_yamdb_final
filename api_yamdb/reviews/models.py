from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    # todo: раскомментировать и заменить IntegerField после объявления моделей юзера и Title
    author = models.IntegerField()  # ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    title = models.IntegerField()  # ForeignKey(Title, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    score = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(10)])
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    # todo: раскомментировать и заменить IntegerField после объявления модели юзера
    author = models.IntegerField()  # ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name='comments')
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text
