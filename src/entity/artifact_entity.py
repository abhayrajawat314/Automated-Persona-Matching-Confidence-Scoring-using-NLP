from dataclasses import dataclass
from typing import Optional

@dataclass
class DataCleaningArtifact:
    cleaned_persona: dict = None

@dataclass
class FeatureExtractionArtifact:
    """
    Artifact produced by Feature Extraction component.
    Attributes:
        features_file_path: Path to JSON file containing the extracted features.
        embeddings_file_path: Path to file (e.g. .pkl) containing serialized embeddings.
        queries_file_path: Path to JSON file containing generated search queries.
    """
    features_file_path: Optional[str] = None
    embeddings_file_path: Optional[str] = None
    queries_file_path: Optional[str] = None