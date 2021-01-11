from django.db import models


class Post(models.Model):
	title = models.CharField(max_lenght=50)
	slug = models.SlugField(max_lenght=20, null=False, blank=False)
	tags = models.TagsField('Tag', max_lenght=20)
	body = models.TextField(max_lenght=200, null=False, blank=False)
	seo_title = models.CharField(max_lenght=50, null=True, blank=True)
	seo_description = models.CharField(max_lenght=200, null=True, blank=True)


class Tag(Meta):
        verbose_name = "tag"
        verbose_name_plural = "tags"
        ordering = ['title']

   

def __srt__(self):
	return self.title
