from . import views
from django.urls import path, register_converter
from . import converters
app_name='subjects'


register_converter(converters.SubjectConverter,'subject')
register_converter(converters.LessonConverter,'lesson')


urlpatterns = [
    path('',views.subject_list,name='subject-list'),
    path('<subject:subject>/',views.subject_detail,name='subject-detail'),

    ## Enrollments
    path('enroll/',views.enroll_subjects,name='enroll-subjects'),
    path('unenroll/',views.unenroll_subjects,name='unenroll-subjects'),

    ## Marks
    path('<subject:subject>/marks/',views.mark_list,name='mark-list'),
    path('<subject:subject>/marks/edit/',views.edit_marks,name='edit-marks'),

    ## Certificates
    path('certificate/',views.request_certificate,name='request-certificate'),

    ## Lessons
    path('<subject:subject>/lessons/add/',views.lesson_add,name='add-lesson'),
    path('<subject:subject>/lessons/<lesson:lesson>/',views.lesson_detail,name='lesson-detail'),
    path('<subject:subject>/lessons/<lesson:lesson>/edit/',views.lesson_edit,name='edit-lesson'),
    path('<subject:subject>/lessons/<lesson:lesson>/delete/',views.lesson_delete,name='delete-lesson'),
]
