import pytest
from task_manager import TaskManager
from models import Base, Task
from config import engine
from confest import add_task

class TestTaskManager:
    
    @classmethod
    def setup_class(cls):
        Base.metadata.create_all(engine)
    
    def setup_method(self):
        self.manager = TaskManager()
        # delete task table
        self.manager.db.query(Task).delete()
        self.manager.db.commit()
        
    def teardown_method(self):
        self.manager.close()
    
    def test_add_task(self):
        self.manager.add_task('Test Task')
        tasks = self.manager.db.query(Task).all()
        assert(len(tasks) == 1)
        assert(tasks[0].description == 'Test Task')

    def test_update_task_success(self, add_task):
        # Setup
        id = add_task('test update_task')
        except_result = True
        # Action
        actual_resutl = self.manager.update_task(id, 'update successfully')
        # Assert
        assert(actual_resutl == except_result)
    
    def test_update_task_fail(self):
        # Setup
        task_id = 999
        except_result = False
        # Action
        acutal_result = self.manager.update_task(task_id, 'test failed')
        # Assert
        assert(acutal_result == except_result)
    
    def test_delete_task_true(self, add_task):
        # Setup
        id = add_task('test update_task')
        except_result = True
        # Action
        actual_resutl = self.manager.delete_task(id)
        # Assert
        assert(actual_resutl == except_result)
        
    def test_delete_task_fail(self):
        # Setup
        task_id = 999
        except_result = False
        # Action
        acutal_result = self.manager.delete_task(task_id)
        # Assert
        assert(acutal_result == except_result)
    
    @pytest.mark.parametrize('status',[('in-progress'),('done')])
    def test_mark_task_success(self, add_task, status):
        # Setup
        id = add_task('test mark_task')
        except_result = True
        # Action
        actual_resutl = self.manager.mark_task(status,id)
        # Assert
        assert(actual_resutl == except_result)
    
    @pytest.mark.parametrize('status',[('in-progress'),('done')])
    def test_mark_task_fail(self,status):
        # Setup
        task_id = 999
        except_result = False
        # Action
        actual_resutl = self.manager.mark_task(status,id)
        # Assert
        assert(actual_resutl == except_result)
        
    
