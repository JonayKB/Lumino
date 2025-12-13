from django.core.management.base import BaseCommand, CommandError
from subjects.models import Enrollment, Subject



class Command(BaseCommand):
    help = 'Get average score from each subject'

    def handle(self, *args, **options):
        subjects = Subject.objects.all()
        for subject in subjects:
            marks = subject.enrollments.filter(mark__isnull=False)
            marks_len = len(marks)

            if marks_len > 0:
                marks_sum = sum(mark.mark for mark in marks)
                marks_avg = marks_sum / marks_len
            else:
                marks_avg = 0.00

            formatted_average = f'{marks_avg:.2f}'
            self.stdout.write(f'{subject.code}: {formatted_average}')
