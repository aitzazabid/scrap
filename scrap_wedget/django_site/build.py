#!/usr/bin/env python
"""
Build file for site; compiles less stylesheets and copies static resources
(images, fonts, javascript files) to output directories.
"""
from sys import argv
from util import static_build

config = {
    # Source directories and the matching output dir.
    'dirs': [
        ('src', 'static'),
        ('webadmin/src', 'static'),
    ],
    # Root less files expected in each less dir; any may be missing.
    'less_files': ['admin'],
}

static_build.build(config, len(argv) > 1)
