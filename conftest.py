
import pytest

from src.infotainment import Infotainment
from src.instrument_cluster import InstrumentCluster


@pytest.fixture
def infotainment():

    system = Infotainment()
    system.start_system()

    return system


@pytest.fixture
def cluster():

    system = InstrumentCluster()
    system.start_system()

    return system
