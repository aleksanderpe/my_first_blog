from django.db import models
from django.utils import timezone

class Post(models.Model):
    economy = "EC"
    world = "WRLD"
    market = "MRKT"
    category_choices = ((economy, "economy"), (world, "world"), (market, "market"))
    post_title = models.CharField(max_length = 500, default = "Post Title")
    content = models.TextField(default = "Content")
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)
    visit_counter = models.IntegerField(default=0)
    category = models.CharField(
        max_length = 7,
        choices = category_choices,
        default = "world")

    def __str__(self):
        return self.post_title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def visit_counter_increase(self):
        self.visit_counter = self.visit_counter + 1
        self.save()
    