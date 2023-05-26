from .settings import *


DEBUG = False

env = environ.Env()
env.read_env(str(BASE_DIR / '.env'))

S3_BUCKET_NAME = env('S3_BUCKET_NAME')
STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
AWS_S3_BUCKET_NAME_STATIC = S3_BUCKET_NAME

# to serve the static files from your s3 bucket
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % S3_BUCKET_NAME
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN