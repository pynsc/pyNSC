from __future__ import absolute_import, division, print_function
import os.path as op
import numpy.testing as npt
import NSC as nsc

data_path = op.join(nsc.__path__[0], 'data')


def test_hello_world():
    npt.assert_equal(1 > 0, True)
