import os

api_id = 20346550
api_hash = os.environ.get("API_HASH", "bc79c3bea7a626887bdc0871eecf0327")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "7081036509")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "7081036509")
owner_users = [int(num) for num in osowner_users.split(",")]
