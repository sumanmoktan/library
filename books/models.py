from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse  # Used to generate urls by reversing the URL patterns
from django.db.models.signals import post_save


# Create your models here.

# relation containg all genre of books
class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


##  __str__ method is used to override default string returnd by an object


##relation containing language of books
class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# book relation that has 2 foreign key author language
# book relation can contain multiple genre so we have used manytomanyfield
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000)
    isbn = models.CharField('ISBN', max_length=13)
    genre = models.ManyToManyField(Genre)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    pic = models.ImageField(blank=True, null=True, upload_to='book_image')

    ##  __str__ method is used to override default string returnd by an object
    def __str__(self):
        return self.title


# relation containing info about students
# roll_no is used for identifing students uniquely
class Student(models.Model):
    roll_no = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)
    branch = models.CharField(max_length=3)
    contact_no = models.CharField(max_length=10)
    total_books_due = models.IntegerField(default=0)
    email = models.EmailField(unique=True)
    pic = models.ImageField(blank=True, upload_to='profile_image')

    def __str__(self):
        return str(self.roll_no)


# relation containing info about Borrowed books
# it has  foriegn key book and student for refrencing book nad student
# roll_no is used for identifing students
# if a book is returned than corresponding tuple is deleted from database
class Borrower(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    issue_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.student.name + " borrowed " + self.book.title


class Reviews(models.Model):
    review = models.CharField(max_length=100, default="none")
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    CHOICES = (
        ('0', '0'),
        ('.5', '.5'),
        ('1', '1'),
        ('1.5', '1.5'),
        ('2', '2'),
        ('2.5', '2.5'),
        ('3', '3'),
        ('3.5', '3.5'),
        ('4', '4'),
        ('4.5', '4.5'),
        ('5', '5'),
    )

    rating = models.CharField(max_length=3, choices=CHOICES, default='2')
