import json
from channels import Group
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible

from .settings import MSG_TYPE_MESSAGE

# Create your models here.
@python_2_unicode_compatible
class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

    @property
    def websocket_group(self):
        """
        Returns the Channels Group that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return Group("room-%s" % self.id)
    
    def __str__(self):
        return self.label

    def send_message(self, message, user, msg_type=MSG_TYPE_MESSAGE):
        """
        Called to send a message to the room on behalf of a user.
        """
        final_msg = {'room': str(self.id), 'message': message, 'username': user.username, 'msg_type': msg_type}

        # Send out the message to everyone in the room
        self.websocket_group.send(
            {"text": json.dumps(final_msg)}
        )

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __unicode__(self):
        return '[{timestamp}] {handle}: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime("%m-%d-%Y %H:%M%p")

    def as_dict(self):
        return {'handle': self.handle, 'message': self.message, 'timestamp': self.formatted_timestamp}