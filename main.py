import argparse
from task_manager import TaskManager

def main():
    parser = argparse.ArgumentParser(description='Task Tracker CLI')
    parser.add_argument('command', choices=['add', 'update', 'delete', 'list', 'mark'], help='Command to execute')
    parser.add_argument('arguments', nargs='*', help='Arguments for the command')
    
    args = parser.parse_args()
    
    manager = TaskManager()
    
    if args.command == 'add':
        manager.add_task(args.arguments[0])
    elif args.command == 'list':
        if args.arguments:
            manager.list_tasks(status=args.arguments[0])
        else:
            manager.list_tasks()
    elif args.command == 'delete':
        manager.delete_task(args.arguments[0])
    elif args.command == 'update':
        manager.update_task(args.arguments[0], args.arguments[1])
    elif args.command == 'mark':
        manager.mark_task(args.arguments[0], args.arguments[1])
        

if __name__ == "__main__":
    main()