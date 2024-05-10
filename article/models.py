from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User", verbose_name="YAZAR", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="BAŞLIK",max_length=50)
    content = RichTextField()
    created_date = models.DateField(verbose_name="OLUŞTURMA TARİHİ",auto_now_add=True)
    article_image = models.FileField(blank= True, null=True,verbose_name="")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']
    

class Comment(models.Model):
    article = models.ForeignKey(Article,verbose_name="Makale",on_delete=models.CASCADE,related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="İsim")
    comment_content = models.CharField(max_length=300,verbose_name="Yorum ")
    comment_date = models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return self.comment_author
    class Meta:
        ordering = ['-comment_date']

