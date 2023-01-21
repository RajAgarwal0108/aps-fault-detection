import os
from datetime import datetime

class TrainingPipelineConfig:
     
     def __init__(self):
        self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y_%H%M%S')}")

class DataIngestionConfig:

    def __init__(self):
        self.database_name = "aps"
        self.collection_name = "sensor"
        self.data_ingestion_dir = os.path.join(TrainingPipelineConfig.artifact_dir,"data_ingestion")
    

class DataValidationConfig:...

class DataTransformationConfig:...

class ModelTrainingConfig:...

class ModelEvaluationConfig:...

class ModelPusherConfig:...
