from tess_asteroids import __version__
import pytest
from tess_asteroid import Asteroid


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.remote_data
def test_asteroid():
    tpf = Asteroid.from_MAST("Juno")
    lc = tpf.to_lightcurve()
    per = lc.to_periodogram("GP", minimum_period=0.1, maximum_period=10)
    assert (per.period_at_max_power[0].value, 10)
    assert (per.period_at_max_power[1].value, 0.1)
