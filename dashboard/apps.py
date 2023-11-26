from django.apps import AppConfig

class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'

    def ready(self):
        from .models import Feedback
        from datetime import datetime

        if Feedback.objects.count() == 0:
            with open('data/feedback_form_data.tsv', 'r') as file:
                lines = file.readlines()
                for line in lines[1:]:
                    values = line.strip().split('\t')
                    dateString = values[0].strip().split(' ')[0]
                    feedback = Feedback(
                        timestamp = datetime.strptime(dateString, '%m/%d/%Y'),
                        teacher_name = values[1],
                        name_of_school = values[2],
                        activity_covered = values[3],
                        total_students = int(values[4]),
                        total_female_students = int(values[5]),
                        total_groups_formed = int(values[6]),
                        total_groups_completed_activity = int(values[7]),
                        do_students_form_groups = True if values[8] == 'Yes' else False,
                        do_students_ask_questions = values[9],
                        initiative_taken_by = values[10],
                        student_sentiment_after_class = values[11],
                        other_feedback = values[12],
                        name_of_block = values[13],
                        state = values[14],
                        date_received = values[15] if values[15] else datetime.strptime(dateString, '%m/%d/%Y'),
                        disctrict = values[16]
                    )
                    feedback.save()
            print('Data Loaded to Database Successfully')
