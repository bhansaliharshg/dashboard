from django.shortcuts import render

from dashboard.forms import UploadFileForm
from .models import Feedback
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
import json
from datetime import datetime
from django.http import HttpResponse

@ensure_csrf_cookie
@csrf_exempt
def index(request):
    all_states = [
        "Andaman and Nicobar Islands","Andra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chandigarh", "Chhattisgarh",
        "Dadra and Nagar Haveli", "Daman and Diu", "Delhi", "Goa","Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir",
        "Jharakhand", "Karnataka", "Kerala", "Ladakh", "Lakshadweep", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland",
        "Odisha", "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
    ]
    #feedbacks = Feedback.objects.all()
    file_uploaded = False
    error = ''
    if request.method == 'POST':
        try:
            requestData = request.POST
            state = requestData['state']
            if state:
                deletedfeedbacks = Feedback.objects.filter(state=state).delete()
                if requestData['reset'] and requestData['reset'] == "False":
                    state_data = requestData['file_data']
                    for data in json.loads(state_data):
                        dateString = data['timestamp'].strip().split(' ')[0]
                        feedback = Feedback(
                            timestamp = datetime.strptime(dateString, '%m/%d/%Y'),
                            teacher_name =  data['teacher_name'],
                            name_of_school = data['name_of_school'],
                            activity_covered = data['activity_covered'],
                            total_students = int(data['total_students']),
                            total_female_students = int(data['total_female_students']),
                            total_groups_formed = int(data['total_groups_formed']),
                            total_groups_completed_activity = int(data['total_groups_completed_activity']),
                            do_students_form_groups = True if data['do_students_form_groups'] == 'Yes' else False,
                            do_students_ask_questions = data['do_students_ask_questions'],
                            initiative_taken_by = data['initiative_taken_by'],
                            student_sentiment_after_class = data['student_sentiment_after_class'],
                            other_feedback = data['other_feedback'],
                            name_of_block = data['name_of_block'],
                            state = state,
                            date_received = data['date_received'] if data['date_received'] else datetime.strptime(dateString, '%m/%d/%Y'),
                            disctrict = data['disctrict']
                        )
                        feedback.save()
                    file_uploaded = True
            else:
                error = 'State not Selected while uplaoding State Data.'
        except json.JSONDecodeError:
            error = 'Something Went Wrong. Please check File Format(.tsv).'
    return render(request, 'dashboard/home.html', {'all_data': json.dumps(list(Feedback.objects.all().values()), cls=DjangoJSONEncoder), 'all_states': all_states, 'error': error, 'file_uploaded': file_uploaded})
