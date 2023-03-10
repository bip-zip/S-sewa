from django.db import models
from django.utils import timezone
from user_auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
from tinymce.models import HTMLField
from django.template.defaultfilters import date
from django.utils.text import slugify


class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', default=1)
    body = HTMLField()
    excerpt = models.TextField(null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(upload_to="pics", null=True, blank=True)
    tags = TaggableManager()
    views = models.IntegerField(default=1)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:articledetail',
        args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)




    @property
    def published(self):
        return '%s' % date(self.publish, "F d, Y")
    
    @property
    def related_posts(self):
        return Post.objects.filter(category = self.category).order_by('views').exclude(id=self.pk)[:6]