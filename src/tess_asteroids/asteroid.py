"""Class to obtain, correct and analyze TESS asteroid data"""
import lightkurve as lk

import tess_ephem
import tess_locator
import tess_cloud
import tess_backdrop


class Asteroid(lk.TargetPixelFile):
    """Class to work with TESS asteroid data"""

    def __init__(self, asteroid_name):
        self.asteroid_name = asteroid_name
        self._correct_sky_background()
        self._correct_star_background()

    @static_method
    def from_MAST(self, asteroid_name):
        """Get object out of tesscut dataset"""
        self.asteroid_name = asteroid_name
        self._get_data()
        self.__init__(**kwargs)

    def _get_data(self):
        """Use tess_locator, tess_cloud"""
        raise NotImplementedError

    def _correct_sky_background(self):
        """Use tess_backdrop to correct scattered light"""
        raise NotImplementedError

    def _correct_star_background(self):
        """Use tess_backdrop, and new functionality, to remove stars from background"""
        raise NotImplementedError

    def create_aperture(self):
        """create_threshold_mask may work just as well here, but we might want to think about
        special functions"""
        raise NotImplementedError

    def to_lightcurve(self):
        """makes special lk.LightCurve class?"""
        raise NotImplementedError


class AsteroidLightCurve(lk.LightCurve):
    """I think we might need a special lk class...but maybe not?"""

    def get_MPC_data(self):
        # Get supplmental data from MPC?
        raise NotImplementedError

    def to_periodogram(self, type="GP"):
        """Special periodogram that uses GP kernels to estimate period?"""
        raise NotImplementedError

    def to_file(self):
        """Some sort of MPC viable file with relevant meta info..."""
        raise NotImplementedError
