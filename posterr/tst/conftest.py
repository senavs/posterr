import pytest

from posterr.src import Bootloader


@pytest.fixture(autouse=True)
def set_up():
    Bootloader(reset=True)
