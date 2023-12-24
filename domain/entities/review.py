import datetime
from typing import NamedTuple

class reviewEntity(NamedTuple):
    reviewId: str
    userName: str
    userImage: str
    content: str
    score: int
    thumbsUpCount: int
    reviewCreatedVersion: str
    at: str
    replyContent: str
    repliedAt: str
    appVersion: str