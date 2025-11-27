S3StorageExample

This project demonstrates how to configure Django to store uploaded media files directly in Amazon S3 instead of the local filesystem. It includes full integration using django-storages and boto3, allowing Django’s file fields to automatically upload to an S3 bucket.
The project is built with Django 5.2.8 and uses a custom storage backend to manage media uploads under a dedicated media/ prefix inside the S3 bucket. This ensures clean folder organization, unique file handling, and proper public URL generation for displaying uploaded images.



🚀 Features

- Upload media files directly to Amazon S3

- Custom Django storage backend using django-storages

- Automatic creation of media/ folder inside the S3 bucket

- Public, CDN-ready URLs for all uploaded files

- Secure configuration using environment variables

- Compatible with Django Admin and any ImageField/FileField



🛠️ Technologies Used

- Django 5.2.8
- django-storages
- boto3 (AWS SDK for Python)
- Amazon S3
- Python-dotenv for environment variable management


📁 Project Structure 
Storagesexample/
├── manage.py
├── requirements.txt
├── .env
├── Storagesexample/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── example/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── migrations/



🧩 How It Works

- Django is configured to use storages.backends.s3boto3.S3Boto3Storage as the default file storage backend.
- When a file is uploaded through Django Admin or any form, storages.backends.s3boto3.S3Boto3Storage automatically:
- Sends the file to your S3 bucket
- Places it inside the media/ directory
- Returns a public URL like: https://yourbucket.s3.your-region.amazonaws.com/media/filename.jpg This allows images and files to load seamlessly in your application without relying on the local filesystem.



🧰 Installation & Setup

1. Clone the Repository git clone cd Storagesexample

2️. Create Virtual Environment python -m venv env source env/bin/activate # Linux/macOS env\Scripts\activate # Windows

3️. Install Dependencies pip install -r requirements.txt

(If you don’t have a requirements.txt, you need at least:) pip install django boto3 django-storages python-dotenv



🔐 AWS Configuration

1️⃣ Create an IAM User

Go to AWS IAM Console

Create user → Programmatic access

Attach policy:

Minimum IAM Permissions { "Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "s3:PutObject", "s3:GetObject", "s3:ListBucket" ], "Resource": [ "arn:aws:s3:::yourbucket", "arn:aws:s3:::yourbucket/*" ] } ] } Generate the Access Key ID and Secret Access Key.


🪣 2️⃣ Create an S3 Bucket

- Go to S3 → Create bucket
- Disable Block Public Access
- Enable ACLs
- Region example: us-west-2



🌍 3️⃣ Bucket Policy (Public Read) { "Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": "", "Action": "s3:GetObject", "Resource": "arn:aws:s3:::yourbucket/" } ] }



🔑 Environment Variables (.env)

- Create a .env file in your project root:
- SECRET_KEY=your-django-secret AWS_ACCESS_KEY_ID=your-key AWS_SECRET_ACCESS_KEY=your-secret AWS_STORAGE_BUCKET_NAME=yourbucket AWS_S3_REGION_NAME=us-west-2
- Django loads this automatically via: from dotenv import load_dotenv load_dotenv()



⚙️ Relevant Django Settings

- AWS S3 Settings
- AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID") AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY") AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME") AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME", "us-east-1") AWS_QUERYSTRING_AUTH = False AWS_DEFAULT_ACL = None AWS_S3_FILE_OVERWRITE = False
- STORAGES = { "default": { "BACKEND": "storages.backends.s3boto3.S3Boto3Storage", "OPTIONS": { # 'location': 'media', }, }, "staticfiles": { "BACKEND": "storages.backends.s3boto3.S3Boto3Storage", "OPTIONS": { "location": "static", }, }, }
- Use S3 URLs for serving files

STATIC_URL = ( f"https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/static/" ) MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/"



📤 Usage


- Run the server: python manage.py runserver
- Upload a file in Django Admin
- Go to:http://127.0.0.1:8000/admin/
- Upload an image using a model with: image = models.ImageField(upload_to="")


Check your bucket

Uploaded files will appear in: media/yourfile.jpg