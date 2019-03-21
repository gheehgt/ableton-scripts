# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-

import Live
from gtroll_twister import gtroll_twister

def create_instance(c_instance):
    ' Creates and returns the APC20 script '
    return gtroll_twister(c_instance)


# local variables:
# tab-width: 4
