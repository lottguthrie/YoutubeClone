SECRET_KEY = 'django-insecure-$*f9va+9a$(i8-iuw()lo-8dzr-r(ikqgc0%jf+9425@#m1)dz'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_clone_database',
        'USER': 'root',
        'PASSWORD': 'SGsg2205$$2205',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}