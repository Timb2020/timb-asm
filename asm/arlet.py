from django.core.mail import send_mail
 
send_mail(
    'Subject here',
    'Here is the message.',
    'danielmutemachani@timb.co.zw',
    ['danielmshaty@timb.co.zw'],
    fail_silently=False,
)