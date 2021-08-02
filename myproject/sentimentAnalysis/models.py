from django.contrib import admin
from django.db import models

# Create your models here.


class InputText(models.Model):
    input_text = models.TextField(max_length=1000)
    input_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.input_text

    def predict(self):
        """
        predict the text using NLP classifier
        """
        return

    @admin.display(
        boolean=True,
        description='Was the machine correct?'
    )
    def incremental_learn(self, feedback: bool):
        """
        incremental learn from the feedback
        """
        return
