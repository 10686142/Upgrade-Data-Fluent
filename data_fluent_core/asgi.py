import os

from django.core.asgi import get_asgi_application
from .websocket import websocket_applciation

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_fluent_core.settings')

django_application = get_asgi_application()

# An ASGI application is a single async function which takes in 3 parameters:
# 1. scope: the context of the current request
# 2. receive: an async function that lets you listen for incoming events
# 3. send: an async function that lets you send events to the client
# You can route requests based on values in the scope dictionary
async def application(scope, receive, send):
    # The request is a normal HTTP request and we should let Django handle it
    if scope['type'] == 'http':
        # Let Django handle HTTP requests
        await django_application(scope, receive, send)
    # We'll want to handle the logic ourselves
    elif scope['type'] == 'websocket':
        # We'll handle Websocket connections here
        await websocket_applciation(scope, receive, send)
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")
