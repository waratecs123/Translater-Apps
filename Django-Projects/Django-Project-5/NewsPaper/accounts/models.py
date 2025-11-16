from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    topic = models.CharField(max_length=255, unique=True)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account_author')
    rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = 3 * sum(post.rating for post in self.post_set.all())
        comment_rating = sum(comment.rating for comment in self.user.comment_set.all())
        post_comment_rating = sum(Comment.objects.filter(post__author=self).values_list('rating', flat=True))
        self.rating = post_rating + comment_rating + post_comment_rating
        self.save()

article = "AR"
news = "NE"

CHOICE_1 = [
    (article, "Статья"),
    (news, "Новость")
]

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    news_choice_article = models.CharField(choices=CHOICE_1, max_length=2, default="NE")
    heading = models.CharField(max_length=255)
    text_n_ar = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text_n_ar[:124] + "..." if len(self.text_n_ar) >= 124 else self.text_n_ar

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account_comments')
    text_com = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()