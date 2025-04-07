from typing import List, Any
from datetime import datetime, timedelta
from time import sleep
import colorama

colorama.init()


class Developer:
    def __init__(self, id: int, name: str, address: str, phone_number: str,
                 email: str, position: int, salary: float) -> None:
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.position = position
        self.salary = salary
        self.assignments = []
        self.projects: List[Project] = []

    def assign_projects(self) -> List[Any]:
        return self.projects

    def assigned(self, project):
        if project not in self.projects:
            self.projects.append(project)

    def unassigned(self, project):
        if project in self.projects:
            self.projects.remove(project)


class Assignment:
    def __init__(self, received_tasks: list[dict], is_done: bool, description: str,
                 status: str) -> None:
        self.received_tasks = received_tasks
        self.is_done = is_done
        self.description = description
        self.status = status

    def get_tasks_to_date(self, start_date: datetime, loop: bool):
        while True:
            res = ""
            self.is_done = True
            for task in self.received_tasks:
                if task.get("is_done") is not False or task.get("date") < datetime.now():
                    res += f"\n{task.get('title')}: \033[32m100% - Done!\033[39m"
                    task["is_done"] = True
                else:
                    self.is_done = False
                    total_time = (task.get("date") - start_date).total_seconds()
                    time_left = (task.get("date") - datetime.now()).total_seconds()
                    progress = int(100 - (time_left / total_time * 100))
                    res += f"\n{task.get('title')}: {progress}%"
            print(res)

            if loop:
                sleep(0.5)
                print("\u001b[5A")
                if self.is_done:
                    print("\u001b[3B")
                    self.status = "Done"
                    return True
            else:
                print("\u001b[1B")
                break


class Project:
    def __init__(self, title: str, task_list: list[dict], limit: int, date: datetime):
        self.title = title
        self.start_date = date
        self.task_list = task_list
        self.limit = limit
        self.developers = []

    def add_developer(self, developer: Developer) -> None:
        if self.limit > len(self.developers) and developer not in self.developers:
            self.developers.append(developer)
            developer.assigned(project=self)

    def remove_developer(self, developer: Developer) -> None:
        if developer in self.developers:
            self.developers.remove(developer)
            print(f"Developer {developer.name} deleted")
            return 0
        print(f"Developer {developer.name} does not exist in this project")
        return 0


class QAEngineer:
    def __init__(self, id: int, name: str, address: str, phone_number: str,
                 email: str, salary: float, rank: str, position: str) -> None:
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary
        self.rank = rank
        self.position = position

    def test_feature(self, assig: Assignment):
        print(f"Description: {assig.description}\nis done: {assig.is_done}\nTasks count: {len(assig.received_tasks)}\n")
        return


class ProjectManager:
    def __init__(self, id: int, name: str, address: str, phone_number: str,
                 email: str, salary: float, project: Project) -> None:
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary
        self.project = project

    def discuss_progress(self, developer: Developer):
        print(f"Developer name: {developer.name} | id - {developer.id}\nemail: {developer.email}\naddress: {developer.address}\nAssignments: {developer.assignments}")
        return


if __name__ == "__main__":
    # Створюємо розробника
    DataDev = Developer(
        id=1,
        name="Mike",
        address="639 Norma Lane, Shreveport, Louisiana",
        phone_number="3185609929",
        email="mike639@gmail.com",
        position="Data Dev",
        salary=500
    )

    # Створюємо список задач із дедлайнами через 15–17 секунд
    task_list = []
    date = datetime.now()
    for i in range(3):
        task_list.append({
            "title": f"messdata-{i+1}",
            "is_done": False,
            "date": date + timedelta(seconds=i + 15)
        })

    # Створюємо проект
    Messenger = Project(
        limit=1,
        title="Messenger",
        task_list=task_list,
        date=date
    )

    # Створюємо Assignment
    MessAssign = Assignment(
        received_tasks=task_list,
        is_done=False,
        description="Work in Messenger Project",
        status="in progress"
    )

    # Прив'язуємо assignment до розробника
    DataDev.assignments.append(MessAssign)

    # Додаємо розробника до проекту
    Messenger.add_developer(DataDev)

    # Запускаємо моніторинг виконання завдань
    MessAssign.get_tasks_to_date(date, loop=True)
