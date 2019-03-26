
import os
from .constants import AD_SHOW, AD_SEQ, AD_SHOT

class LevelSpec(object):
    def __init__(self, show, seq=None, shot=None):
        self._show = show
        self._seq = seq if show is not None else None
        self._shot = shot if seq is not None else None

    def is_valid(self):
        return self._show is not None

    @property
    def show(self):
        return self._show

    @property
    def seq(self):
        return self._seq

    @property
    def sequence(self):
        return self._seq

    @property
    def shot(self):
        return self._shot

    @classmethod
    def from_str(cls, value):
        pieces = value.split(".")
        assert len(pieces) < 4, "invalid level spec"
        return cls(*pieces)

    @classmethod
    def from_env(cls):
        args = [os.environ.get(AD_SHOW), os.environ.get(AD_SEQ), os.environ.get(AD_SHOT)]
        return cls(*args)

    def __str__(self):
        return ".".join(filter(lambda x: x is not None, (self.show, self.seq, self.shot)))

    def path(self):
        """
        retrieve a path fragment
        """
        path = os.path.join(*filter(lambda x: x is not None, (self.show, self.seq, self.shot)))
        return path