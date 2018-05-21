import os
from authlib.django.client import OAuth

RACO_CLIENT_ID = os.getenv('RACO_CLIENT_ID')
RACO_CLIENT_SECRET = os.getenv('RACO_CLIENT_SECRET')
RACO_AUTH_URL = os.getenv('RACO_AUTH_URL')

oauth = OAuth()
oauth.register('raco',
               client_id=RACO_CLIENT_ID,
               client_secret=RACO_CLIENT_SECRET,
               request_token_url=None,
               request_token_params=None,
               access_token_url='https://api.fib.upc.edu/v2/o/token',
               access_token_params=None,
               refresh_token_url='https://api.fib.upc.edu/v2/o/token',
               authorize_url='https://api.fib.upc.edu/v2/o/authorize',
               api_base_url='https://api.fib.upc.edu/v2/',
               client_kwargs={'response_type': 'code', 'scope': 'read', 'approval_prompt': 'force'},
               )
