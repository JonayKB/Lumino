from django_rq import job
from django.conf import settings
from weasyprint import HTML

@job
def deliver_certificate(base_url, student: settings.AUTH_USER_MODEL ):
    HTML('subjects/templates/emails/certificate.html', base_url=base_url).write_pdf(f'media/certificates/{student.username}_grade_certificate.pdf')

# from django.core.mail import EmailMessage
# from django.shortcuts import redirect, render
# from django.template.loader import render_to_string

# from markdown import markdown


# @login_required
# def add_post(request):
#     if request.method == 'POST':
#         if (form := AddPostForm(request.POST)).is_valid():
#             post = form.save()
#             body = markdown(render_to_string(
#                 'posts/emails/add.md',
#                 {'post': post}
#             ))
#             email = EmailMessage(
#                 subject='New post',
#                 body=body,
#                 to=['super@blog.com']
#             )
#             email.send()
#             return redirect('posts:post-list')
#     else:
#         form = AddPostForm()
#     return render(request, 'posts/post/add.html', {'form': form})
