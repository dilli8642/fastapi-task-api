from sqlmodel import select, Session
from .models import User, Task
from .schemas import UserCreate, TaskCreate, TaskUpdate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# -------------------------
# Users
# -------------------------
def get_user_by_username(session: Session, username: str):
    statement = select(User).where(User.username == username)
    return session.exec(statement).first()

def create_user(session: Session, user: UserCreate):
    hashed = pwd_context.hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def authenticate_user(session: Session, username: str, password: str):
    user = get_user_by_username(session, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

# -------------------------
# Tasks
# -------------------------
def create_task(session: Session, owner_id: int, task: TaskCreate):
    db_task = Task(**task.dict(), owner_id=owner_id)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

def get_task(session: Session, task_id: int):
    return session.get(Task, task_id)

def list_tasks(session: Session, owner_id: int | None = None, q: str | None = None):
    statement = select(Task)
    if owner_id is not None:
        statement = statement.where(Task.owner_id == owner_id)
    if q:
        statement = statement.where((Task.title.contains(q)) | (Task.description.contains(q)))
    return session.exec(statement.order_by(Task.created_at.desc())).all()

def update_task(session: Session, task_id: int, task_in: TaskUpdate):
    db_task = get_task(session, task_id)
    if not db_task:
        return None
    obj_data = task_in.dict(exclude_unset=True)
    for key, val in obj_data.items():
        setattr(db_task, key, val)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

def delete_task(session: Session, task_id: int):
    db_task = get_task(session, task_id)
    if not db_task:
        return False
    session.delete(db_task)
    session.commit()
    return True
