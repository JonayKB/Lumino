from django_rq import job
from django.conf import settings
from django.template.loader import render_to_string
from weasyprint import HTML
from django.core.mail import EmailMessage

from django.utils.translation import gettext as _

@job
def deliver_certificate(base_url, student: settings.AUTH_USER_MODEL):
    #Para traducir el mensaje, lo unico que requeriria es en esta llamada recibir el lang, ya que el metodo de get_language no funciona ya que no hay request
    #Una vez lo tuvieramos, solo habria que seleccionarlo, y usarlo en la plantilla o en la llamada de gettext

    content = render_to_string('emails/certificate.html', {'student': student})
    pdfPath = f'media/certificates/{student.username}_grade_certificate.pdf'

    HTML(string=content, base_url=base_url).write_pdf(pdfPath)

    email = EmailMessage(
        subject=f'{_("Grade Certificate for")} {student.profile.get_full_name()}',
        body=content,
        to=[student.email]
    )
    email.attach_file(pdfPath)
    email.send()
