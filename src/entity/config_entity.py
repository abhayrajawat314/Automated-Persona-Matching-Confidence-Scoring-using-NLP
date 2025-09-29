import os
from dataclasses import dataclass
from datetime import datetime
from src.constants import ARTIFACT_DIR, TIMESTAMP, DATA_CLEANING_DIR_NAME, CLEANED_FILE_NAME
from src.constants import FEATURE_EXTRACTION_DIR_NAME, FEATURES_FILE_NAME, EMBEDDINGS_FILE_NAME, QUERIES_FILE_NAME


@dataclass
class DataCleaningConfig:
    data_cleaning_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP, DATA_CLEANING_DIR_NAME)
    cleaned_file_name: str = CLEANED_FILE_NAME

    @property
    def cleaned_file_path(self) -> str:
        return os.path.join(self.data_cleaning_dir, self.cleaned_file_name)


@dataclass
class FeatureExtractionConfig:
    base_artifact_dir: str = ARTIFACT_DIR
    timestamp: str = TIMESTAMP
    component_name: str = FEATURE_EXTRACTION_DIR_NAME

    def __post_init__(self):
        self.artifact_dir = os.path.join(self.base_artifact_dir, self.timestamp, self.component_name)
        os.makedirs(self.artifact_dir, exist_ok=True)

        self.features_file = os.path.join(self.artifact_dir, FEATURES_FILE_NAME)
        self.embeddings_file = os.path.join(self.artifact_dir, EMBEDDINGS_FILE_NAME)
        self.queries_file = os.path.join(self.artifact_dir, QUERIES_FILE_NAME)
