import datetime
from typing import NamedTuple

class reviewDTO(NamedTuple):
    reviewId: str
    userName: str
    userImage: str
    content: str
    score: int
    thumbsUpCount: int
    reviewCreatedVersion: str
    at: str
    replyContent: str
    repliedAt: datetime.datetime
    appVersion: str