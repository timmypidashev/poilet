# -*- coding: utf-8 -*-

"""
MIT License

Copyright (c) 2022 Timothy Pidashev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse

from .version import __version__

class PoiletError(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return self.error


def main():
    parser = argparse.ArgumentParser(
        prog='poilet',
        usage='%(prog)s [options]',
        description='Python variant of The Other Implementation of figLET'
    )
    parser.add_argument(
        '-v', '--version', required=False, help='output version information and exit', metavar=''
    )
    args = parser.parse_args()
