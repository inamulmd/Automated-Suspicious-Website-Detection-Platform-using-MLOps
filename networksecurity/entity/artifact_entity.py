from dataclasses import dataclass
#@dataclass automatically generates constructor (__init__), representation (__repr__), comparison methods, and more.

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str


@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path:str
    drift_report_file_path: str

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str
    transformed_train_file_path: str
    transformed_test_file_path: str


@dataclass
class ClassificationMetricArtifact:
    f1_score:float
    precision_score: float
    recall_score:float

@dataclass
class ModeTrainerArtifact:
    trained_model_file_path:str
    train_metric_artifact: ClassificationMetricArtifact 
    test_metric_artifact:ClassificationMetricArtifact     
