from django.shortcuts import render
from .models import Feedback
from django.db.models import Sum, Count
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
import json
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
    feedbacks = Feedback.objects.all()
    if request.method == 'POST':
        try:
            files = request.FILES['file']
            print(files)
        except json.JSONDecodeError:
            print('ERROR')
    #     male_attendance, female_attenadance, male_vs_female_attenadance, total_students = getAttendance(feedbacks)
    #     groups_formed, groups_completed_activity = getGroups(feedbacks)
    #     questions_asked = getQuestions(feedbacks)
    #     takes_initiative = getInitiatives(feedbacks)
    #     states_and_districts = getStatesAndDistricts(feedbacks)
    #     students_sentiment = getStudentSentiments(feedbacks)
    # return render(request, 'dashboard/home.html', { "all_data": json.dumps(list(feedbacks.values()), cls=DjangoJSONEncoder), "new_visitors" : male_attendance, "returning_visitors": female_attenadance,
    #                                                "new_vs_returning_visitors": male_vs_female_attenadance, "totalAttendance": total_students,
    #                                                "groups_formed" : groups_formed, "groups_completed_activity": groups_completed_activity,
    #                                                'questions_asked': questions_asked, 'takes_intiative':takes_initiative,
    #                                                'states_and_districts': states_and_districts, 'students_sentiment': students_sentiment, 'all_states': all_states})
    return render(request, 'dashboard/home.html', {'all_data': json.dumps(list(feedbacks.values()), cls=DjangoJSONEncoder), 'all_states': all_states})


# def getStatesAndDistricts(feedbacks):
#     statesAndDistricts = {}
#     states_and_districts = []
#     garbage_values = ["NA", "", "N/A", "#N/A", "N\A","#N\A"]
#     for feedback in feedbacks:
#         if feedback.state not in statesAndDistricts:
#             statesAndDistricts[feedback.state] = {'district':[feedback.disctrict], 'block': [feedback.name_of_block]}
#         else:
#             if feedback.disctrict not in statesAndDistricts[feedback.state]['district'] and feedback.disctrict not in garbage_values:
#                 statesAndDistricts[feedback.state]['district'].append(feedback.disctrict)
#             if feedback.name_of_block not in statesAndDistricts[feedback.state]['block'] and feedback.name_of_block not in garbage_values:
#                 statesAndDistricts[feedback.state]['block'].append(feedback.name_of_block)
#     for key, value in statesAndDistricts.items():
#         states_and_districts.append({'state':key,'districts':value['district'],'blocks':value['block']})
#     return states_and_districts

# def getStudentSentiments(feedbacks):
#     total_records = int(feedbacks.count())
#     students_sentiment = []
#     studentSentiemnts = feedbacks.values('student_sentiment_after_class').annotate(count=Count('student_sentiment_after_class'))
#     for sentiment in studentSentiemnts:
#         students_sentiment.append({'label':sentiment['student_sentiment_after_class'], 'y':sentiment['count']*100/total_records})
#     return students_sentiment



# def getInitiatives(feedbacks):
#     total_records = int(feedbacks.count())
#     takesInitiative = feedbacks.values('initiative_taken_by').annotate(count=Count('initiative_taken_by'))
#     takes_initiative = []
#     for initiative in takesInitiative:
#         takes_initiative.append({'label':initiative['initiative_taken_by'], 'y': initiative['count']*100/total_records})
#     return takes_initiative

# def getAttendance(feedbacks):
#     total_students = feedbacks.aggregate(total_students=Sum('total_students'))['total_students']
#     total_female_students = feedbacks.aggregate(total_females=Sum('total_female_students'))['total_females']
#     male_attenadance = []
#     maleAttendance = {}
#     female_attenadance = []
#     femaleAttendance = {}
#     for feedback in feedbacks:
#         dateString = feedback.date_received.strftime('%d-%m-%Y')
#         if dateString not in maleAttendance:
#             maleAttendance[dateString] = feedback.total_students - feedback.total_female_students
#         else:
#             maleAttendance[dateString] += feedback.total_students - feedback.total_female_students
#         if dateString not in femaleAttendance:
#             femaleAttendance[dateString] = feedback.total_female_students
#         else:
#             femaleAttendance[dateString] += feedback.total_female_students
#     for key, value in femaleAttendance.items():
#         female_attenadance.append({'label':key, 'y': value})
#     for key,value in maleAttendance.items():
#         male_attenadance.append({'label':key, 'y':value})
#     male_vs_female_attenadance = [
#         { "name": "Male Attendance", "y": total_students - total_female_students, "color": "#DF7970" },
#         { "name": "Female Attendance", "y": total_female_students, "color": "#4C9CA0" },
#     ]
#     return male_attenadance, female_attenadance, male_vs_female_attenadance, total_students

# def getGroups(feedbacks):
#     groups_formed = []
#     groups_completed_activity = []
#     groups = {
#         'totalGroupsFormed': {},
#         'totalGroupsCompletedActivity': {}
#     }
#     for feedback in feedbacks:
#         dateString = feedback.date_received.strftime('%d-%m-%Y')
#         if dateString not in groups['totalGroupsFormed']:
#                 groups['totalGroupsFormed'][dateString] = feedback.total_groups_formed
#         else:
#             groups['totalGroupsFormed'][dateString] += feedback.total_groups_formed
#         if dateString not in groups['totalGroupsCompletedActivity']:
#             groups['totalGroupsCompletedActivity'][dateString] = feedback.total_groups_completed_activity
#         else:
#             groups['totalGroupsCompletedActivity'][dateString] += feedback.total_groups_completed_activity
#     for key,value in groups['totalGroupsFormed'].items():
#         groups_formed.append({'label':key, 'y':value})
#     for key,value in groups['totalGroupsCompletedActivity'].items():
#         groups_completed_activity.append({'label':key, 'y':value})
#     return groups_formed, groups_completed_activity

# def getQuestions(feedbacks):
#     questionsAsked = {}
#     questions_asked = []
#     for feedback in feedbacks:
#         if feedback.do_students_ask_questions not in questionsAsked:
#             questionsAsked[feedback.do_students_ask_questions] = 1
#         else:
#             questionsAsked[feedback.do_students_ask_questions] += 1
#     for key, value in questionsAsked.items():
#         questions_asked.append({'label':key, 'y':value})
#     return questions_asked
