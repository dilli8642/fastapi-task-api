from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from .database import init_db, get_session, engine
from .schemas import UserCreate, UserRead, Token, TaskCreate, TaskRead, TaskUpdate
from .crud import create_user, authenticate_user as crud_authenticate, create_task, list_tasks, get_task, update_task, delete_task, get_user_by_username
from .auth import create_access_token, get_current_user
from .models import User
from typing import List

app = FastAPI(title="Task Manager API")

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/register", response_model=UserRead)
def register(user_in: UserCreate):
    with Session(engine) as session:
        existing = get_user_by_username(session, user_in.username)
        if existing:
            raise HTTPException(status_code=400, detail="Username already registered")
        user = create_user(session, user_in)
        return user

@app.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud_authenticate(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post('/tasks/auth/', response_model=TaskRead)
def create_task_auth(task_in: TaskCreate, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    return create_task(session, owner_id=user.id, task=task_in)

@app.get('/tasks/auth/', response_model=List[TaskRead])
def read_tasks_auth(q: str | None = None, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    return list_tasks(session, owner_id=user.id, q=q)

@app.get('/tasks/auth/{task_id}', response_model=TaskRead)
def read_task_auth(task_id: int, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    task = get_task(session, task_id)
    if not task or task.owner_id != user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put('/tasks/auth/{task_id}', response_model=TaskRead)
def update_task_auth(task_id: int, task_in: TaskUpdate, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    task = get_task(session, task_id)
    if not task or task.owner_id != user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    updated = update_task(session, task_id, task_in)
    return updated

@app.delete('/tasks/auth/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task_auth(task_id: int, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    task = get_task(session, task_id)
    if not task or task.owner_id != user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    delete_task(session, task_id)
    return None

@app.get('/tasks/', response_model=List[TaskRead])
def list_public_tasks(q: str | None = None, session: Session = Depends(get_session)):
    return list_tasks(session, owner_id=None, q=q)
