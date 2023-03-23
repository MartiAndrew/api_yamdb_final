import csv

from django.conf import settings
from django.core.management.base import BaseCommand
from reviews.models import Category, Comment, Genre, Review, Title
from user.models import User

LENGTH_TEXT = 25


class DataBaseExceptionError(Exception):
    """Ошибка базы данных"""


class Command(BaseCommand):
    help = 'Импортирует данные из CSV-файлов в базу данных'

    def load_category(self):
        path = f'{settings.BASE_DIR}/static/data/category.csv'
        with open(path, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            try:
                for row in reader:
                    reviews_category = Category.objects.create(
                        name=row[1],
                        slug=row[2]
                    )
                    self.stdout.write(self.style.SUCCESS(
                        f'Category {reviews_category.name} создан.'
                    ))
            except Category.DoesNotExist:
                self.stderr.write(self.style.ERROR('Category не создан'))
            except ValueError as error:
                self.stderr.write(self.style.ERROR(f'Error: {str(error)}'))

    def load_genre(self):
        path = f'{settings.BASE_DIR}/static/data/genre.csv'
        with open(path, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            try:
                for row in reader:
                    reviews_genre = Genre.objects.create(
                        name=row[1],
                        slug=row[2]
                    )
                    self.stdout.write(self.style.SUCCESS(
                        f'Genre {reviews_genre.name} создан.'
                    ))
            except Genre.DoesNotExist:
                self.stderr.write(self.style.ERROR('Genre не создан'))
            except ValueError as error:
                self.stderr.write(self.style.ERROR(f'Error: {str(error)}'))

    def load_titles(self):
        path = f'{settings.BASE_DIR}/static/data/titles.csv'
        with open(path, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            try:
                for row in reader:
                    reviews_title = Title.objects.create(
                        name=row[1],
                        year=row[2],
                        category_id=row[3],
                    )
                    self.stdout.write(self.style.SUCCESS(
                        f'Title {reviews_title.name} создан.'
                    )
                    )
            except Title.DoesNotExist:
                self.stderr.write(self.style.ERROR('Title  не создан'))
            except ValueError as error:
                self.stderr.write(self.style.ERROR(f'Error: {str(error)}'))

    def load_users(self):
        path = f'{settings.BASE_DIR}/static/data/users.csv'
        with open(path, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            try:
                for row in reader:
                    user_user = User.objects.create(
                        id=row[0],
                        username=row[1],
                        email=row[2],
                        role=row[3],
                        bio=row[4],
                        first_name=row[5],
                        last_name=row[6]
                    )
                    self.stdout.write(self.style.SUCCESS(
                        f'User {user_user.username} создан.'
                    )
                    )
            except User.DoesNotExist:
                self.stderr.write(self.style.ERROR('User не создан'))

            except ValueError as error:
                self.stderr.write(self.style.ERROR(f'Error: {str(error)}'))

    def load_reviews(self):
        path = f'{settings.BASE_DIR}/static/data/review.csv'
        with open(path, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            try:
                for row in reader:
                    user_id = row[3]
                    try:
                        user_user = User.objects.get(id=user_id)
                    except User.DoesNotExist:
                        user_user = User.objects.create(id=user_id)
                    try:
                        reviews_review = Review.objects.create(
                            id=row[0],
                            title_id=row[1],
                            text=row[2],
                            author_id=user_id,
                            score=row[4],
                            pub_date=row[5],
                            author=user_user
                        )
                        self.stdout.write(self.style.SUCCESS(
                            f'Review "{reviews_review.text[:LENGTH_TEXT]}" '
                            f'создан.'
                        ))
                    except Review.DoesNotExist:
                        self.stderr.write(self.style.ERROR('Review не создан'))
                    except ValueError as error:
                        self.stderr.write(self.style.ERROR(f'Error: '
                                                           f'{str(error)}'))
            except DataBaseExceptionError as error:
                self.stderr.write(self.style.ERROR(f'Error: {str(error)}'))

    def load_comments(self):
        path = f'{settings.BASE_DIR}/static/data/comments.csv'
        with open(path, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            try:
                for row in reader:
                    user_id = row[3]
                    try:
                        user_user = User.objects.get(id=user_id)
                    except User.DoesNotExist:
                        user_user = User.objects.create(id=user_id)
                    try:
                        reviews_comment = Comment.objects.create(
                            id=row[0],
                            review_id=row[1],
                            text=row[2],
                            author_id=user_id,
                            pub_date=row[4],
                            author=user_user
                        )
                        self.stdout.write(self.style.SUCCESS(
                            f'Comment "{reviews_comment.text[:LENGTH_TEXT]}" '
                            f'создан.'
                        ))
                    except Comment.DoesNotExist:
                        self.stderr.write(
                            self.style.ERROR('Comment не создан'))
                    except ValueError as error:
                        self.stderr.write(self.style.ERROR(f'Error: '
                                                           f'{str(error)}'))
            except DataBaseExceptionError as error:
                self.stderr.write(self.style.ERROR(f'Error: {str(error)}'))

    def load_genre_titles(self):
        path = f'{settings.BASE_DIR}/static/data/genre_title.csv'
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                title_id = row[1]
                genre_id = row[2]
                try:
                    title = Title.objects.get(id=title_id)
                    genre = Genre.objects.get(id=genre_id)
                    title.genre.add(genre)
                    self.stdout.write(self.style.SUCCESS(
                        f'Успешно добавлен genre "{genre}" в произведение'
                        f'"{title}"'))
                except (Title.DoesNotExist, Genre.DoesNotExist,):
                    self.stderr.write(self.style.ERROR(
                        'Произведение/Жанр не создан'))
                except DataBaseExceptionError as error:
                    self.stderr.write(self.style.ERROR(f'Error: {str(error)}'))

    def handle(self, *args, **options):
        self.load_category()
        self.load_genre()
        self.load_titles()
        self.load_users()
        self.load_genre_titles()

        self.stdout.write(self.style.SUCCESS('База данных импортирована '
                                             'полностью.'))
