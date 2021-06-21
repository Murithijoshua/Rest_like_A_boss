from typing import SupportsRound
from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source ='owner.username')
    owner_id = serializers.ReadOnlyField(source = 'owner.id')
    class Meta:
        model = Post
        fields = ['id', 'title','url','created','owner', 'owner_id']


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote 
        fields = ['id']