import os, sys, re, json
from src.logger import logging
from src.exception import MyException
from src.entity.config_entity import DataCleaningConfig
from src.entity.artifact_entity import DataCleaningArtifact

class DataCleaning:
    def __init__(self, data_cleaning_config: DataCleaningConfig):
        try:
            self.data_cleaning_config = data_cleaning_config
            logging.info(f"DataCleaning component initialized with dir: {self.data_cleaning_config.data_cleaning_dir}")
        except Exception as e:
            raise MyException(e, sys)

    def clean_text(self, text: str):
        if not text or not isinstance(text, str):
            return None
        text = text.strip().lower()
        text = re.sub(r'\s+', ' ', text)
        return text

    def clean_persona(self, persona: dict):
        try:
            logging.info("Starting persona cleaning process...")
            cleaned = {}
            for key, value in persona.items():
                if isinstance(value, str):
                    cleaned[key] = self.clean_text(value)
                else:
                    cleaned[key] = value
            logging.info("Completed persona cleaning process.")
            return cleaned
        except Exception as e:
            raise MyException(e, sys)

    def run_cleaning(self, persona: dict) -> DataCleaningArtifact:
        try:
            cleaned_persona = self.clean_persona(persona)

            os.makedirs(self.data_cleaning_config.data_cleaning_dir, exist_ok=True)
            with open(self.data_cleaning_config.cleaned_file_path, "w", encoding="utf-8") as f:
                json.dump(cleaned_persona, f, indent=4)

            logging.info(f"Saved cleaned persona at {self.data_cleaning_config.cleaned_file_path}")

            return DataCleaningArtifact(cleaned_persona=cleaned_persona)

        except Exception as e:
            raise MyException(e, sys)
