from datetime import datetime

from rukkola.src.domain.base_model import BaseModel


class User:
    ID = int
    CreatedAt = datetime
    Name = str


class UserModel(BaseModel):
    id: User.ID
    created_at: User.CreatedAt
    name: User.Name
