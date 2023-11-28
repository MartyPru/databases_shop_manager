from dataclasses import dataclass

@dataclass
class Post:
    id: int
    title: str
    content: str
    views: int
    account_id: int
