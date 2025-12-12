from django.shortcuts import get_object_or_404

from .models import Profile

class ProfileConverter:
    regex = '[a-zA-Z0-9_-]+'

    def to_python(self, username):
        return get_object_or_404(Profile, user__username=username)

    def to_url(self, profile: Profile):
        return str(profile.user.username)