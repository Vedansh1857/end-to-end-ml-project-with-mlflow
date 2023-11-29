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