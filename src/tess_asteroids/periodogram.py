"""Tools to calculate periodicities in asteroid light curves?"""
import lightkurve as lk


class GPPeriodogram(lk.Periodogram):
    """A periodogram that works based on SHO GP kernels to obtain
    a distribution of consistent periods."""

    def __init__(self, **kwargs):
        """Initialize a normal periodogram..."""
        super.__init__(**kwargs)


class AugmentedBLSPeriodogram(lk.Periodogram):
    """A periodogram that fits a BLS and SHO at the same time, to model binary asteroids."""

    def __init__(self, **kwargs):
        """Initialize a normal periodogram..."""
        super.__init__(**kwargs)
