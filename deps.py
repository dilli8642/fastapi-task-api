from fastapi import Depends
from .database import get_session
from .auth import get_current_user

get_db = Depends(get_session)
current_user = Depends(get_current_user)
