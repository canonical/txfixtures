from six import b

from testtools import TestCase

from twisted.internet import reactor
from twisted.internet.utils import getProcessOutput
from twisted.internet.defer import (
    succeed,
    fail,
)

from txfixtures._twisted.threading import (
    CallFromThreadTimeout,
    interruptableCallFromThread,
)

from txfixtures.reactor import Reactor


class InterruptableCallFromThreadTest(TestCase):

    def setUp(self):
        super(InterruptableCallFromThreadTest, self).setUp()
        self.useFixture(Reactor())

    def test_success(self):
        """
        If the async call executed in the thread succeeds, the result is
        returned.
        """
        self.assertEqual(
            "hello",
            interruptableCallFromThread(reactor, 1, lambda: succeed("hello")))

    def test_fail(self):
        """
        If the async call executed in the thread fails, an exception is raised.
        """
        self.assertRaises(
            RuntimeError, interruptableCallFromThread, reactor, 1,
            lambda: fail(RuntimeError("boom")))

    def test_timeout(self):
        """After setUp is run, the reactor is spinning."""
        self.assertRaises(
            CallFromThreadTimeout, interruptableCallFromThread,
            reactor, 0.1, getProcessOutput, b("/bin/cat"))
