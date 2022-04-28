import os

S3_BUCKET = os.environ.get('S3_BUCKET', 'aixplain-jobserve-io')
S3_KEY_PREFIX = os.environ.get('S3_KEY_PREFIX', 'async-outputs/')
