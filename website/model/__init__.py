"""This file contains all the data structures for the website"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class content:
    creator_id: str
    timestamp: datetime
    content_id: str
    content_type
