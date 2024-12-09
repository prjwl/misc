from app import create_app
import serverless_wsgi

# Initialize the flask app
app = create_app()

def lambda_function(event, context):
    return serverless_wsgi.handle_request(app, event, context)
