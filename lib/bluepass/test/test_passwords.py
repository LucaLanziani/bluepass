#
# This file is part of Bluepass. Bluepass is Copyright (c) 2012
# Geert Jansen. All rights are reserved.

from bluepass.test.unit import UnitTest
from bluepass.passwords import *


class TestPasswordGenerator(UnitTest):

    @classmethod
    def setup_class(cls):
        super(TestPasswordGenerator, cls).setup_class()
        cls.generator = PasswordGenerator()

    def test_generate_random(self):
        gen = self.generator
        pw = gen.generate('random', 20)
        assert isinstance(pw, str)
        assert len(pw) == 20
        pw = gen.generate('random', 20, 'ab')
        assert isinstance(pw, str)
        assert len(pw) == 20
        assert 'a' in pw
        assert 'b' in pw
        pw = gen.generate('random', 20, '[0-9]')
        assert isinstance(pw, str)
        assert len(pw) == 20
        assert pw.isdigit()
        pw = gen.generate('random', 20, '[0-]')
        assert isinstance(pw, str)
        assert len(pw) == 20
        assert '-' in pw
        pw = gen.generate('random', 20, '][[]')
        assert isinstance(pw, str)
        assert len(pw) == 20
        assert '[' in pw
        assert ']' in pw

    def test_generate_diceware(self):
        gen = self.generator
        pw = gen.generate('diceware', 6)
        assert isinstance(pw, str)
        assert len(pw) >= 11
        print pw
        assert pw.count(' ') == 5
