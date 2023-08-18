from allauth.socialaccount.models import SocialAccount
from ..models import Memory


def get_user_social_data(user: str):
    """Logic for displaying user social data"""
    social_data = SocialAccount.objects.get(user=user)
    return social_data


def get_user_memories(user: str):
    """Logic for displaying the user's memories"""
    memories = Memory.objects.filter(user_id=user)
    return memories

