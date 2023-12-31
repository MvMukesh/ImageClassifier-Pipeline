import os
from tqdm import tqdm
from pathlib import Path
from zipfile import ZipFile
import urllib.request as request
from imageClassifier import logger
from imageClassifier.utils import get_size
from imageClassifier.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Trying to download file...")
        if not os.path.exists(self.config.local_data_file):
            logger.info("Download started...")
            filename, headers = request.urlretrieve(url=self.config.source_URL,filename=self.config.local_data_file)
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

           #### --- implementing only unzip code as per requirement --- ###
    # def unzip_file(self):
    #     logger.info(f"unzipping file and removing unawanted files")
    #     with ZipFile(self.config.local_data_file, 'r') as zip_ref:
    #         zip_ref.extractall(self.config.unzip_dir) 
    def unzip_file(self):
        with ZipFile(self.config.local_data_file, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            with tqdm(total=len(file_list), desc="Unzipping") as t:
                for file in file_list:
                    zip_ref.extractall(self.config.unzip_dir)
                    t.update(1)


    # def _get_updated_list_of_files(self, list_of_files):
    #     return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]

    # def _preprocess(self,zf:ZipFile,f:str,working_dir:str):
    #     target_filepath = os.path.join(working_dir,f)
    #     if not os.path.exists(target_filepath):
    #         zf.extract(f, working_dir)
    #     if os.path.getsize(target_filepath) == 0:
    #         logger.info(f"removing file:{target_filepath} of size: {get_size(Path(target_filepath))}")
    #         os.remove(target_filepath)

    # def unzip_and_clean(self):
    #     logger.info(f"unzipping file and removing unawanted files")
    #     with ZipFile(file=self.config.local_data_file,mode="r") as zf:
    #         list_of_files = zf.namelist()
    #         updated_list_of_files = self._get_updated_list_of_files(list_of_files)
    #         for f in tqdm(updated_list_of_files):
    #             self._preprocess(zf, f, self.config.unzip_dir)