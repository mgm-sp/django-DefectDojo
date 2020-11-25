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
            # Get corresponding APIv2 key:
            apiv2key = Token.objects.filter(user=apiv1key.user).first()

            # Print before state:
            print('BEFORE: User: %s, APIv1key: %s, APIv2key: %s' % (
                apiv1key.user.username, apiv1key.key,
                'none' if apiv2key is None else apiv2key.key))

            # Delete old APIv2 key if it exists:
            # NOTE: Updating it doesn't work because the `key` field is the
            #       primary key, so we have to delete the old one and create
            #       a new one.
            if apiv2key is not None:
                apiv2key.delete()

            # Create new APIv2 key:
            apiv2key = Token.objects.create(user=apiv1key.user,
                                            key=apiv1key.key)

            # Print after state:
            print('AFTER: User: %s, APIv1key: %s, APIv2key: %s' % (
                apiv1key.user.username, apiv1key.key, apiv2key.key))
