#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 23:07:23 2019.

@author: mtageld
"""
import unittest
import os
import tempfile
import shutil
from imageio import imread, imwrite
import girder_client
import numpy as np
# from matplotlib import pylab as plt
# from matplotlib.colors import ListedColormap
from histomicstk.preprocessing.color_normalization import reinhard
from histomicstk.saliency.tissue_detection import get_tissue_mask

# %%===========================================================================
# Constants & prep work

APIURL = 'http://candygram.neurology.emory.edu:8080/api/v1/'
SAMPLE_SLIDE_ID = "5d817f5abd4404c6b1f744bb"