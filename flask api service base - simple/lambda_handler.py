import serverless_wsgi

from app import app as application


def lambda_handler(event, context):
    return serverless_wsgi.handle_request(application, event, context)
