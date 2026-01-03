from django_rq import job
from django.conf import settings
from django.template.loader import render_to_string
from weasyprint import HTML
from django.core.mail import EmailMessage
from django.utils.translation import activate
from django.utils.translation import gettext as _

@job
def deliver_certificate(base_url, student: settings.AUTH_USER_MODEL, lang = 'en'):
    activate(lang)
    content = render_to_string('emails/certificate.html', {'student': student})
    pdfPath = f'media/certificates/{student.username}_grade_certificate.pdf'

    HTML(string=content, base_url=base_url).write_pdf(pdfPath)

    email = EmailMessage(
        subject=f'{_("Grade Certificate from")} {student.profile.get_full_name()}',
        body=content,
        to=[student.email]
    )
    email.attach_file(pdfPath)
    email.send()
