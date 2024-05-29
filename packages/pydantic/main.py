from pydantic import BaseModel, ValidationError, Field, validator
from typing import List, Optional
from datetime import datetime


class AdvancedUser(BaseModel):
    id: int = Field(..., gt=0, description="The unique identifier for a user")
    name: str = Field(..., max_length=50)
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

    @validator('name')
    def name_must_be_longer_than_three(cls, v):
        if len(v) < 3:
            raise ValueError('Name must be at least 3 characters long')
        return v

    @validator('friends', each_item=True)
    def friends_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Friend IDs must be positive integers')
        return v




try:
    advanced_user = AdvancedUser(
        id=123,
        name='John Doe',
        signup_ts='2021-05-21T10:20:30.400',
        friends=[1, 2, 3]
    )
    print(advanced_user)
except ValidationError as e:
    print(e.json(indent=2))




try:
    advanced_user = AdvancedUser(
        id=123,
        name='ok',
        signup_ts='2021-05-21T10:20:30.400',
        friends=[1, 2, -3]
    )
    print(advanced_user)
except ValidationError as e:
    print(e.json(indent=2))