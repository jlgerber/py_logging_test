"""
LevelSpec implementation
"""
import os
from .constants import AD_SHOW, AD_SEQ, AD_SHOT

class LevelSpec(object):
    """
    fake levelspec
    """
    def __init__(self, show, seq=None, shot=None):
        """
        initialize given a show and optionally a seq and shot
        """
        self._show = show
        self._seq = seq if show is not None else None
        self._shot = shot if seq is not None else None

    def is_valid(self):
        """
        test whether the show is valid (ie if show is not None)
        """
        return self._show is not None

    @property
    def show(self):
        """
        get show
        """
        return self._show

    @property
    def seq(self):
        """
        get the sequence if you are lazy
        """
        return self._seq

    @property
    def sequence(self):
        """
        also get the sequence
        """
        return self._seq

    @property
    def shot(self):
        """
        get shot
        """
        return self._shot

    @classmethod
    def from_str(cls, value):
        """
        given a levelspec formatted string, return a levelspec object
        """
        pieces = value.split(".")
        assert len(pieces) < 4, "invalid level spec"
        return cls(*pieces)

    @classmethod
    def from_env(cls):
        """
        Construct a levelspec from the environment
        """
        args = [os.environ.get(AD_SHOW), os.environ.get(AD_SEQ), os.environ.get(AD_SHOT)]
        return cls(*args)

    def __str__(self):
        #return ".".join(filter(lambda x: x is not None, (self.show, self.seq, self.shot)))
        return ".".join([x for x in  (self.show, self.seq, self.shot) if x is not None])
    def path(self):
        """
        retrieve a path fragment
        """
        #path = os.path.join(*filter(lambda x: x is not None, (self.show, self.seq, self.shot)))
        path = os.path.join(*[x for x in (self.show, self.seq, self.shot) if x is not None])
        return path
