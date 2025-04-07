import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import Developer, Project
from datetime import datetime

def test_assign_developer_to_project():
    dev = Developer(1, "Test Dev", "123 Street", "123456", "test@example.com", 1, 1000)
    project = Project("Test Project", [], 1, datetime.now())

    project.add_developer(dev)

    assert dev in project.developers
    assert project in dev.assign_projects()
