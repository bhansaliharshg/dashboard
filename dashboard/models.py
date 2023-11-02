from django.db import models
from django.utils import timezone

class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateField()
    teacher_name = models.CharField(max_length=200)
    name_of_school = models.TextField()
    activity_covered = models.CharField(max_length=200)
    total_students = models.PositiveIntegerField()
    total_female_students = models.PositiveIntegerField()
    total_groups_formed = models.PositiveIntegerField()
    total_groups_completed_activity = models.PositiveIntegerField()
    do_students_form_groups = models.BooleanField()
    do_students_ask_questions = models.CharField(max_length=200)
    initiative_taken_by = models.CharField(max_length=200)
    student_sentiment_after_class = models.CharField(max_length=400)
    other_feedback = models.TextField()
    name_of_block = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    date_received = models.DateField()
    disctrict = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.id)+' '+self.state+' '+self.disctrict+' '+self.name_of_block+' '+self.name_of_school+' '+self.teacher_name