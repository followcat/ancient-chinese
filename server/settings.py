DEBUG = True

WX_APPID = 'your appid'
WX_SECRET = 'your app secret'

# Flask settings
SECRET_KEY = 'This is an INSECURE secret!! DO NOT use this in production!!'

# Flask-MongoEngine settings
MONGODB_SETTINGS = {
    'db': 'ancient-chinese',
    'host': 'mongodb://localhost:27017/ancient-chinese'
}

# Flask-User settings
USER_APP_NAME = "Flask-User MongoDB App"      # Shown in and email templates and page footers
USER_ENABLE_EMAIL = False      # Disable email authentication
USER_ENABLE_USERNAME = True    # Enable username authentication
USER_REQUIRE_RETYPE_PASSWORD = False    # Simplify register form
