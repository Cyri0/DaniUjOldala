from django.db import models
from ckeditor.fields import RichTextField
import datetime

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def serialize(self):
        return {'id':self.id, 'tagname':self.name }

class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    intro = models.TextField(max_length=500)
    content = RichTextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    tags = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return self.title

    def serialize(self):

        mytags = self.tags.all()
        tags = []
        for tag in mytags:
            tags.append({'tagid':tag.id,'tagname':tag.name})


        return {
            'postid': self.id,
            'title' : self.title,
            'intro' : self.intro,
            'content' : self.content,
            'created': self.created.strftime('%Y.%m.%d. %H:%M'),
            'updated': self.created.strftime('%Y.%m.%d. %H:%M'),
            'tags' : tags
        }

    def tag_list(self):
        mytags = self.tags.all()
        tags = []
        for tag in mytags:
            tags.append(tag.id)
        return tags