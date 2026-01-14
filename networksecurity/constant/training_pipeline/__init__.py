import os
import sys
import numpy as np
import pandas as pd

# Defining common constant variable for training pipeline
TARGET_COLUMN="label"
PIPELINE_NAME="NetworkSecurity"
ARTIFACT_DIR="Artifact"
FILE_NAME="phishing_dataset.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


# Data Ingestion related constant starts with DATA_INGESTION VAR NAME

DATA_INGESTION_COLLECTION_NAME="NetworkData"
DATA_INGESTION_DATABASE_NAME="RAHULAI"
DATA_INGESTION_DIR_NAME="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT: float = 0.2