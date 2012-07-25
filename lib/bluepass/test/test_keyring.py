#
# This file is part of Bluepass. Bluepass is Copyright (c) 2012
# Geert Jansen. All rights are reserved.

import os
from nose import SkipTest

from bluepass.factory import create
from bluepass.keyring import Keyring, KeyringError
from bluepass.test.unit import UnitTest


class TestKeyring(UnitTest):

    @classmethod
    def setup_class(cls):
        super(TestKeyring, cls).setup_class()
        keyring = create(Keyring)
        if keyring is None or not keyring.isavailable():
            raise SkipTest('This test requires a Keyring to be avaialble')
        cls.keyring = keyring

    def test_roundtrip(self):
        key = os.urandom(8).encode('hex')
        secret = os.urandom(32)
        self.keyring.store(key, secret)
        value = self.keyring.retrieve(key)
        assert value == secret

    def test_overwrite(self):
        key = os.urandom(8).encode('hex')
        for i in range(10):
            secret = os.urandom(i)
            self.keyring.store(key, secret)
            value = self.keyring.retrieve(key)
            assert value == secret
