from .BaseController import BaseController
from fastapi import UploadFile
from helpers.config import get_settings, Settings

class DataController(BaseController): 
    def __init__(self):
        super().__init__()

    def validate_uploaded_file(self, file: UploadFile):
        