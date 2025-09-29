import os
from datetime import datetime

# -------------------- Root Directories --------------------
ROOT_PATH = "c:/Users/Hp/Desktop/Persona Matching"
ARTIFACT_DIR = "artifacts"
DATA_DIR = "data_access"

# -------------------- Timestamp --------------------
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

# -------------------- Component Directories --------------------
DATA_CLEANING_DIR_NAME = "data_cleaning"
FEATURE_EXTRACTION_DIR_NAME = "feature_extraction"

# -------------------- File Names --------------------
# Data Cleaning
CLEANED_FILE_NAME = "cleaned_persona.json"

# Feature Extraction
FEATURES_FILE_NAME = "features.json"
EMBEDDINGS_FILE_NAME = "embeddings.pkl"
QUERIES_FILE_NAME = "queries.json"

# Other constants
TRAIN_TEST_SPLIT_RATIO = 0.2
