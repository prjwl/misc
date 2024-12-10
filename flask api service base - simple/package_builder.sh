# Script to build a zip file which can be deployed on aws lambda

# Create a deployment package
mkdir -p package

# Install dependencies in tha package dir
pip install -r requirements.txt -t package/

# Copy all the app files
cp *.py package/

# Create a zip file
cd package
zip -r ../sample_package.zip .
cd ..
rm -rf package/
