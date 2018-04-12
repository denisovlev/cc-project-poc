from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

import os

raco_client_id = os.environ('RACO_CLIENT_ID')
raco_client_secret = os.environ('RACO_CLIENT_SECRET')
raco_auth_url = os.environ('RACO_AUTH_URL')
