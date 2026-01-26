from dataclasses import dataclass
#@dataclass automatically generates constructor (__init__), representation (__repr__), comparison methods, and more.

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str