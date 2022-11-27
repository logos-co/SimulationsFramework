import json
from dataclasses import dataclass

# yaml_obj = yaml_parser.YamlParser(input_yaml, valid_flags.VALID_FLAGS_PLATFORM)


@dataclass
class SimulationConfig:
    file: str
    data: dict

