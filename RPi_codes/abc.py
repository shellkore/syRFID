import cloudinary
from cloudinary.models import CloudinaryField

result = cloudinary.uploader.unsigned_upload("a.jpg", resource_type = "auto",upload_preset =  'irfrdbpk', cloud_name = 'subhash')

print(result.secure_url)
