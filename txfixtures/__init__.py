from pbr.version import VersionInfo

from .reactor import (
    Reactor,
)

__all__ = [
    "Reactor",
]

_v = VersionInfo("txfixtures").semantic_version()
__version__ = _v.release_string()
version_info = _v.version_tuple()
