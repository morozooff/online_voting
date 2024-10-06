from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List

@dataclass
class ValueObject:
    """Base object"""
    @property
    def to_json(self):
        if isinstance(self, list):
            return [asdict(item) for item in self]
        else: 
            return asdict(self)


@dataclass
class Poll(ValueObject):
    id: int
    question: str
    created_at: datetime
    
@dataclass
class PollList(ValueObject):
    polls: List[Poll]
    
@dataclass
class Choice(ValueObject):
    id: int
    text: str
    votes: int

@dataclass
class PollChoices(ValueObject):
    choices: List[Choice]