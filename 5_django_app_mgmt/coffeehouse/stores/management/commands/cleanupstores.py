from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = 'Clean up stores'
    
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('store_id')
        
        # Named (optional) arguments
        parser.add_argument(
            '--delete',
            default=False,
            help='Delete store instead of cleaning it up',
        )

    def handle(self, *args, **options):
        print(args)
        print(options)
        try:
            if options['delete']:
                # delete flag is present
                self.stdout.write(self.style.WARNING("About to delete store %s" % options['store_id']))
                # Logic to delete store here
                # Any other Python logic can also go here
                self.stdout.write(self.style.SUCCESS('Successfully deleted store "%s"' % options['store_id']))
            else:
                # No delete flag is present
                self.stdout.write(self.style.WARNING("About to clean up store %s" % options['store_id']))
                # Logic to cleaup up store here
                # Any other Python logic can also go here
                self.stdout.write(self.style.SUCCESS('Successfully cleaned up store "%s"' % options['store_id']))                
        except Exception as e:
            raise CommandError('Failed to clean up stores %s' % e)

