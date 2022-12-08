from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class Mailer():
    def __init__(self, subject, fm, to, data, template):
        self.subject = subject

        self.from_email = fm
        self.to = to
        self.template = template
        self.data = data

    def send(self):
        html_body = render_to_string(self.template, self.data)

        message = EmailMultiAlternatives(
          subject= self.subject,
          from_email=self.from_email,
          to=self.to
        )
        message.attach_alternative(html_body, "text/html")
        message.send(fail_silently=False)