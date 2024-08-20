from sqlalchemy.orm import Session
from models import Task, Base
from config import engine, Session

# create the database tables
Base.metadata.create_all(bind=engine)

class TaskManager:
    def __init__(self):
        self.db = Session()
        
    def add_task(self, description:str, status='to-do') -> None:
        new_task = Task(description=description, status=status)
        self.db.add(new_task)
        self.db.commit()
        self.db.refresh(new_task)
        print(f"Task added successfully (ID: {new_task.id})")
    
    
    def update_task(self, id, description,status='to-do') -> bool:
        task = self.db.query(Task).filter(Task.id == id).first()
        
        if task:
            task.description = description
            task.status = status
            self.db.commit()
            return True
        else:
            return False
    
    
    def delete_task(self, id) -> bool:
        task = self.db.query(Task).filter(Task.id == id).first()
        
        if task:
            self.db.delete(task)
            self.db.commit()
            return True
        else:
            return False
    
    
    def mark_task(self, new_status, id) -> bool:
        task = self.db.query(Task).filter(Task.id == id).first()
        
        if task:
            task.status = new_status
            self.db.commit()
            return True
        else:
            return False
    
    def list_tasks(self, status=None):
        if status is not None:
            tasks = self.db.query(Task).filter(Task.status == status).all()
        else:
            tasks = self.db.query(Task).all()

        if tasks:
            for task in tasks:
                print(f'task id is {task.id} | task description is {task.description} | task status is {task.status}')
        
        return tasks

    def close(self):
        """
        close the databese
        """
        self.db.close()