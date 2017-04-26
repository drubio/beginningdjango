from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = 'Send test emails'

    def handle(self, *args, **options):
        for admin_name,email in settings.ADMINS:
            try:
                self.stdout.write(self.style.WARNING("About to send email to %s" % (email)))
                # Logic to send email here
                # Any other Python logic can also go here
                self.stdout.write(self.style.SUCCESS('Successfully sent email to "%s"' % email))
            except Exception as e:
                raise CommandError('Failed to send test email %s' % e)
            




