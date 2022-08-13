import os
from datetime import datetime, timedelta

import pytest


class SetEnv:
    def __init__(self):
        self.envars = set()

    def set(self, name, value):
        self.envars.add(name)
        os.environ[name] = value

    def clear(self):
        for n in self.envars:
            os.environ.pop(n)


@pytest.fixture
def env():
    setenv = SetEnv()
    yield setenv
    setenv.clear()


@pytest.fixture
def date():
    return datetime.today() - timedelta(days=15)


@pytest.fixture
def start_time():
    return datetime.today() - timedelta(days=15, minutes=5)


@pytest.fixture
def end_time():
    return datetime.today() - timedelta(days=15)


@pytest.fixture
def start_times():
    return [
        datetime.today() - timedelta(days=15, minutes=5),
        datetime.today() - timedelta(days=16, minutes=5),
    ]


@pytest.fixture
def end_times():
    return [
        datetime.today() - timedelta(days=15),
        datetime.today() - timedelta(days=16),
    ]
