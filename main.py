from typing import List, Any
from datetime import datetime, timedelta
from time import sleep
import colorama
colorama.init()

class Developer:
    # Ініціалізуємо клас
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

    # Метод повертає проекти розробника
    def assign_projects(self) -> List[Any]:
        return self.projects

    # Метод додає проект якщо він ще не наявний
    def assigned(self, project):
        if project not in self.projects:
            self.projects.append(project)

    # Метод видалення проекту якщо він наявний
    def unassigned(self, project):
        if project in self.projects:
            self.projects.remove(project)


class Assignment:

    # Ініціалізуємо клас
    def __init__(self, received_tasks: list[dict], is_done: bool, description: str,
                 status: str) -> None:
        self.received_tasks = received_tasks
        self.is_done = is_done
        self.description = description
        self.status = status

    # Метод перевірки виконання тасків
    def get_tasks_to_date(self, start_date: datetime, loop: bool):
        while(True):
            res = ""
            self.is_done = True
            for task in self.received_tasks:
                if task.get("is_done") != False or task.get("date") < datetime.now():
                    res += f"\n{task.get('title')}: \033[32m100% - Done!\033[39m"
                    task["is_done"] = True
                else:
                    self.is_done = False
                    res += f"\n{task.get('title')}: {int(100-((task.get('date') - datetime.now()).total_seconds()//((task.get('date') - start_date).total_seconds()/100)))}%"
            print(res)
            if loop == True:
                sleep(0.5)
                print("\u001b[5A")
                if self.is_done == True:
                    print("\u001b[3B")
                    self.status = "Done"
                    return True
            else:
                print("\u001b[1B")
                break


class Project:

    # Ініціалізуємо клас
    def __init__(self, title: str, task_list: list[dict], limit: int, date: datetime):
        self.title = title
        self.start_date = date
        self.task_list = task_list
        self.limit = limit
        self.developers = []

    # Метод додавання розробника якщо він не наявний та не перевищує ліміт розробників
    def add_developer(self, developer: Developer) -> None:
        if self.limit > len(self.developers) and developer not in self.developers:
            self.developers.append(developer)
            developer.assigned(project=self)

    # Метод видалення розробника якщо він наявний
    def remove_developer(self, developer: Developer) -> None:
        if developer in self.developers:
            self.developers.remove(developer)
            print(f"Developer {developer.name} deleted")
            return 0
        print(f"Developer {developer.name} does not exist in this project")
        return 0

class QAEngineer:
    # Ініціалізуємо клас
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

    # Інформація про роботу
    def test_feature(self, assig: Assignment):
        print(f"Description: {assig.description}\nis done: {assig.is_done}\nTasks count: {len(assig.received_tasks)}\n")
        return


class ProjectManager:
    # Ініціалізуємо клас
    def __init__(self, id: int, name: str, address: str, phone_number: str,
                 email: str, salary: float, project: Project) -> None:
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary
        self.project = project

    # Інфо про розробника
    def discuss_progress(self, developer: Developer):
        print(f"Developer name: {developer.name} | id - {developer.id}\nemail: {developer.email}\naddress: {developer.address}\nAssigments: {developer.assignments}")
        return


if __name__ == "__main__":
    # Створюємо розробника
    DataDev = Developer(id=1, name="Mike", address="639 Norma Lane, Shreveport, Louisiana", phone_number="3185609929",
                        email="mike639@gmail.com", position="Data Dev", salary=500)
    # Створюємо пустий список тасків
    task_list =[]
    # Заповнюємо список тасків із закінченням через 1-3 хв від часу створення
    date = datetime.now()
    #task_list.append({"title": "messdata-1", "is_done": False, "date": date + timedelta(seconds=21)})
    for i in range(3):
        task_list.append({"title": "messdata" + str(i), "is_done": False, "date": date + timedelta(seconds=i+15)})
    # Створюємо проект
    Messenger = Project(limit=1, title="messenger", task_list=task_list, date=date)
    # Створюємо роботу
    MessAssign = Assignment(description="Work in Mess. Project", is_done=False, status="in progress", received_tasks=task_list)
    DataDev.assignments.append(MessAssign)
    Messenger.add_developer(developer=DataDev)
    MessAssign.get_tasks_to_date(date, True)