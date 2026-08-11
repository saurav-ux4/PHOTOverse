import cloudinary
import cloudinary.api
import config.cloudinary

try:
    result = cloudinary.api.ping()
    print("Cloudinary connection successful!")
    print(result)
except Exception as e:
    print("Cloudinary connection failed:")
    print(e)