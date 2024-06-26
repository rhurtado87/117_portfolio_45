from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class ProjectsPageView(TemplateView):
    template_name = 'pages/projects.html'

class ContactsPageView(TemplateView):
    template_name = 'pages/contact.html'


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            email_to = "ricardohurtado@yahoo.com"
            email_from = form.cleaned_data['email']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']

            # Constructing HTML message for email
            html_message = render_to_string('email/contact_email.html', {
                'name': name,
                'message': message,
                'email': email_from,
            })

            send_mail(
                "Message from " + name,
                message,
                settings.EMAIL_HOST_USER,
                [email_to],
                html_message=html_message,
            )

            return redirect("about")  # Redirect to 'about' page after successful submission

    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})
