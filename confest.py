import pytest
from task_manager import TaskManager
from models import Task

@pytest.fixture
def add_task():
    def _add_task(description):
        manager = TaskManager()
        manager.add_task(description)
        new_task = manager.db.query(Task).filter(Task.description == description).first()
        task_id = new_task.id
        manager.db.commit()
        manager.close()
        return task_id
    return _add_task