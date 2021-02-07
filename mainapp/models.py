from django.db import models


class Post(models.Model):
    """Post model"""
    username = models.CharField('username', max_length=100, default='')
    description = models.CharField('description', max_length=500, default='')
    image = models.ImageField('Image', upload_to='images/')

    def __str__(self):
        return str(self.id)

    def get_comments(self):
        return self.comment_set.filter()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    username = models.CharField('username', max_length=100)
    text = models.CharField('text', max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
