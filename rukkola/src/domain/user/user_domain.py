from datetime import datetime

from rukkola.src.domain.base_model import BaseEntity


class User:
    ID = int
    CreatedAt = datetime
    Name = str


class UserEntity(BaseEntity):
    id: User.ID
    created_at: User.CreatedAt
    name: User.Name
