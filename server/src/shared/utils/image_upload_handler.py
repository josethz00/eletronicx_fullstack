import uuid
import boto3
from config import variables


class ImageUploadHandler:

    def __init__(self):
        self.__alowed_types = (
            'jpeg',
            'png',
            'bmp',
            'JPEG',
            'jpg',
            'JPG',
            'PNG',
            'BMP'
        )
        self.__s3 = boto3.client(
            's3',
            aws_access_key_id=variables.S3_ACCESS_KEY,
            aws_secret_access_key=variables.S3_SECRET_ACCESS_KEY
        )

    def uploadFile(self, file_data) -> str:
        new_filename = self.validateFile(file_data)

        if file_data and new_filename:
            file_data.filename = new_filename
            upload_link = self.uploadFileToS3(file_data, variables.S3_BUCKET)
            return upload_link

    def validateFile(self, file_data) -> str or Exception:
        read = file_data.read()
        name = file_data.filename

        if len(read) > 2 * (1024 ** 2):
            raise ValueError('File too large')

        points = name.split('.')
        file_ext = points[len(points) - 1]

        if file_ext in self.__alowed_types:
            return f'luby_test{str(uuid.uuid4())}.{file_ext}'

        raise TypeError('This file type is not allowed')

    def uploadFileToS3(
        self,
        file,
        bucket_name: str,
        acl: str = 'public-read'
    ) -> str:
        self.__s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                'ACL': acl,
                'ContentType': file.content_type
            }
        )
        return "{}{}".format(variables.S3_LOCATION, file.filename)
