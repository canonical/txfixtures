"""Extensions to Twisted's stock testing helpers."""

import signal

from twisted.test.proto_helpers import MemoryReactorClock

EXPECTED_SIGNALS = (signal.SIGTERM, signal.SIGTERM)


class ThreadedMemoryReactorClock(MemoryReactorClock):
    """Extend Twisted's test reactor with more reactor-level features.

    :ivar async: A flag indicating whether callFromThread calls should be
        executed synchronously as soon as callFromThread is called.
    """

    def __init__(self):
        super(ThreadedMemoryReactorClock, self).__init__()
        self.async = False
        self._internalReaders = set()

    def run(self, installSignalHandlers=False):
        super(ThreadedMemoryReactorClock, self).run()
        self.installSignalHandlers = installSignalHandlers
        self.running = True

    def crash(self):
        super(ThreadedMemoryReactorClock, self).crash()
        self.running = False

    def callFromThread(self, f, *args, **kwargs):
        if self.async:
            return
        f(*args, **kwargs)

    def addReader(self, reader):
        reader.install = lambda: setattr(reader, "installed", True)
        super(ThreadedMemoryReactorClock, self).addReader(reader)
