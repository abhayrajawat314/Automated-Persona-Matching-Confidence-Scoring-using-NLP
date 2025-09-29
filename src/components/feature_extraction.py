import os
import json
import joblib
import logging
from dataclasses import dataclass
from datetime import datetime
from sentence_transformers import SentenceTransformer
from src.entity.config_entity import FeatureExtractionConfig
from src.entity.artifact_entity import FeatureExtractionArtifact


class FeatureExtraction:
    """
    A class to handle feature extraction, embedding generation, 
    and search query construction for persona data.
    """

    def __init__(self, cleaned_data: dict, config: FeatureExtractionConfig):
        """
        Initialize the FeatureExtraction class with cleaned persona data.

        Args:
            cleaned_data (dict): Dictionary containing cleaned persona data.
            config (FeatureExtractionConfig): Configuration object containing artifact paths.
        """
        self.cleaned_data = cleaned_data
        self.config = config
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def extract_features(self) -> dict:
        """
        Extracts structured features from persona data.

        Returns:
            dict: Extracted features with keys such as name, company, role, etc.
        """
        try:
            features = {
                "name": self.cleaned_data.get("Name"),
                "company": self.cleaned_data.get("Company"),
                "role": self.cleaned_data.get("Role"),
                "location": self.cleaned_data.get("Location"),
                "education": self.cleaned_data.get("Education")
            }
            features = {k: v for k, v in features.items() if v}

            with open(self.config.features_file, "w") as f:
                json.dump(features, f, indent=4)

            logging.info("Features extracted and saved.")
            return features
        except Exception as e:
            logging.error(f"Error extracting features: {e}")
            raise

    def create_embeddings(self, features: dict) -> dict:
        """
        Generates sentence embeddings for the extracted features.

        Args:
            features (dict): Extracted features.

        Returns:
            dict: Dictionary with feature embeddings.
        """
        try:
            embeddings = {k: self.model.encode(v) for k, v in features.items()}
            joblib.dump(embeddings, self.config.embeddings_file)

            logging.info("Embeddings created and saved.")
            return embeddings
        except Exception as e:
            logging.error(f"Error creating embeddings: {e}")
            raise

    def build_search_queries(self, features: dict) -> list:
        """
        Builds search queries for LinkedIn based on extracted features.

        Args:
            features (dict): Extracted features.

        Returns:
            list: List of search queries.
        """
        try:
            queries = []
            name = features.get("name")
            company = features.get("company")
            role = features.get("role")
            location = features.get("location")

            if name:
                queries.append(f"{name} linkedin")
            if name and company:
                queries.append(f"{name} {company} linkedin")
            if name and role:
                queries.append(f"{name} {role} linkedin")
            if name and company and location:
                queries.append(f"{name} {company} {location} linkedin")
            if name and role and company:
                queries.append(f"{name} {role} {company} linkedin")

            with open(self.config.queries_file, "w") as f:
                json.dump(queries, f, indent=4)

            logging.info("Queries built and saved.")
            return queries
        except Exception as e:
            logging.error(f"Error building queries: {e}")
            raise

    def run(self) -> FeatureExtractionArtifact:
        """
        Executes the feature extraction pipeline and returns an artifact describing
        the produced files.
        """
        try:
            features = self.extract_features()
            self.create_embeddings(features)
            self.build_search_queries(features)

            artifact = FeatureExtractionArtifact(
                features_file_path=self.config.features_file,
                embeddings_file_path=self.config.embeddings_file,
                queries_file_path=self.config.queries_file
            )

            logging.info("🚀 Feature Extraction pipeline completed successfully.")
            return artifact

        except Exception as e:
            logging.error(f"Pipeline execution failed: {e}")
            raise
