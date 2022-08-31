from django.db import models
from companies.models import Company


class JobPost(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.DO_NOTHING,
        related_name='job_post',
        null=True,
        blank=True,
    )

    position = models.TextField()

    reward = models.IntegerField(default=0)

    contents = models.TextField()

    tech_stack = models.TextField()

    class Meta:
        verbose_name = '채용공고'
        db_table = 'job_posts'
