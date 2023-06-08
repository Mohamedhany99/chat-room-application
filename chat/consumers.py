# your_app/consumers.py
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class NotificationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'notifications'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive_json(self, content):
        # Process the received message and send it to the group
        message = content.get('message')
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_notification',
                'message': message,
            }
        )

    async def send_notification(self, event):
        message = event['message']
        await self.send_json({
            'message': message,
        })