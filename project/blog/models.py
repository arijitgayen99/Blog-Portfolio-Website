from __future__ import unicode_literals
from djongo import models

class Blogposts(models.Model):
	created_at = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated_at = models.DateTimeField(auto_now_add = False, auto_now = True)

	author = models.CharField(max_length = 20, null = False)
	title = models.CharField(max_length = 50, null = False)
	content = models.CharField(max_length = 1000, null = False)

	date_posted = models.CharField(max_length = 20, null = False)

	def __str__(self):
		return self.author	