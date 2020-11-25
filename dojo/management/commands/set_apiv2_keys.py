from django.core.management.base import BaseCommand
from tastypie.models import ApiKey
from rest_framework.authtoken.models import Token


"""
Author: Robert Knauer
This scripts sets the APIv2 key of all users to the APIv1 key, if it exists.
For users that don't have an APIv1 key, it does nothing.
"""


class Command(BaseCommand):
    help = 'Set all APIv2 keys to the values of the corresponding APIv1 keys'

    def handle(self, *args, **options):
        # Get all APIv1 keys:
        for apiv1key in ApiKey.objects.all():
            # Get or create corresponding APIv2 key:
            apiv2key, _ = Token.objects.get_or_create(user=apiv1key.user)

            # Print before state:
            print('BEFORE: User: %s, APIv1key: %s, APIv2key: %s' % (
                apiv1key.user.username, apiv1key.key, apiv2key.key))

            # Set APIv2 key to APIv1 key:
            apiv2key.key = apiv1key.key
            apiv2key.save()

            # Print after state:
            print('AFTER: User: %s, APIv1key: %s, APIv2key: %s' % (
                apiv1key.user.username, apiv1key.key, apiv2key.key))
