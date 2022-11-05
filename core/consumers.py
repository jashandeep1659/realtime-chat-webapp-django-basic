from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive_json(self, content):
        data = content
        if data["command"] == "join":
            await self.channel_layer.group_add("public", self.channel_name)
        elif data["command"] == "send":
            # print(self.scope["user"])
            # print(data["message"])
            await self.channel_layer.group_send(
                "public",
                {
                    "type": "chat.message",
                    "message": data["message"],
                    "user": str(self.scope["user"]),
                },
            )

    async def disconnect(self, msg):
        pass

    async def chat_message(self, event):
        await self.send_json(
            {
                "message": event["message"],
                "user": event["user"],
            }
        )
