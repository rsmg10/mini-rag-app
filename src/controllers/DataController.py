from .BaseController import BaseController
from fastapi import UploadFile
from helpers.config import get_settings, Settings
from models import ResponseSignal

class DataController(BaseController): 
    def __init__(self):
        super().__init__()
        self.size_scale = 10485672 # 1 MB in bytes
    def validate_uploaded_file(self, file: UploadFile):
        
        if(file.content_type not in self.app_settings.FILE_ALLOWED_TYPES):
            return False, ResponseSignal.FILE_TYPE_NOT_ALLOWED.value
        if(file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale):
            return False, ResponseSignal.FILE_SIZE_EXCEED.value
        return True, ResponseSignal.FILE_UPLOAD_SUCCESS.value