from django.shortcuts import render
from django.views import View
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import EmailForm
from .models import Email


class EmailAttachmentView(View):
    form_class = EmailForm
    model = Email
    template_name = 'email_app/email.html'

    def get(self, request,  *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'email_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        print('******', form.is_valid())
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            files = request.FILES.getlist('attach')

            try:
                email_msg = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
                for f in files:
                    email_msg.attach(f.name, f.read(), f.content_type)
                email_msg.send()
                return render(request, self.template_name,
                              {'email_form': form, 'error_message': 'Sent email to %s' % email})

            except Exception as e:
                print(e)
                return render(request, self.template_name,
                              {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

        return render(request, self.template_name,
                 {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})