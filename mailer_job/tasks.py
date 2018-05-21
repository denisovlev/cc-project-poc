from main.models import Post
from mailer_job.celery import app
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives


@app.task
def send_emails():
    # retrieve emails not sent from model Post

    # Set maximum emails sent per job. Set to None to send all emails.
    MAX_EMAILS = 2
    try:
        #when retrieving notifications, order them from old to new (to know if one modifies the other) ASCENDING
        new_posts = Post.objects.filter(email_sent=False).order_by("modification_date")

        for post in new_posts[0:MAX_EMAILS]:

            #send email
            print(post.title)
            print(post.user.email)


            subject = 'Racó Notifications: ' + post.subject + ' - ' + post.title
            from_email, to = 'raconotifications@gmail.com', post.user.email
            text_content = 'Published at: ' + str(post.modification_date) + ' Content: ' + post.text
            html_content = 'Published at: ' + str(post.modification_date) + '<br> ' + post.text
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")

            #iterate through attachments of this post
            attachments = post.attachment_set.all()
            for attach in attachments:
                msg.attach(attach.name, attach.content, attach.mime)

            msg.send()





            #set email_sent as True in model Post
            post.email_sent = True
            post.save()

    except Exception as inst:
        print(type(inst))
        print(inst.args)