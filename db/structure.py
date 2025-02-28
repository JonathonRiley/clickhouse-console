from dataclasses import dataclass
from typing import List

@dataclass
class Column:
    name: str
    type: str
    default_type:str=None
    default_expression:str=None
    comment:str=None
    codec_expression:str=None
    ttl_expression:str=None


@dataclass
class Table:
    name: str
    columns: List[Column] = None


@dataclass
class Database:
    name: str
    tables: List[Table] = None

@dataclass
class Structure:
    databases: List[Database] = None
