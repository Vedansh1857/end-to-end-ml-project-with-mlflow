from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig():
    root_dir:Path
    local_data_file:Path
    download_dir:Path

@dataclass(frozen=True)
class Datavalidationconfig():
    root_dir:Path
    file_dir:Path
    status_file:str
    all_schema:dict

@dataclass(frozen=True)
class DataTransformationConfig():
    root_dir:Path
    data_path:Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    criterion: str
    n_estimators: int
    target_column: str

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str