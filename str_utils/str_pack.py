# -*- coding: utf-8 -*-
import re


class StrPack(object):
    """str utils"""

    def __init__(self, string: str):
        self.string = string

    def camelcase2underline(self):
        """
        convert camelcase str to underline str
        :return:
        """
        p = re.compile(r'([a-z]|\d)([A-Z])')
        s = re.sub(p, r'\1_\2', self.string).lower()
        return s

    def underline2camelcase(self):
        """
        convert underline str to camelcase
        :return:
        """
        s = re.sub(r'(_\w)', lambda x: x.group(1)[1].upper(), self.string)
        return s


if __name__ == '__main__':
    # strPack = StrPack("trackName")
    # underline = strPack.camelcase2underline()
    # print(underline)
    strPack = StrPack("track_name")
    camelcase = strPack.underline2camelcase()
    print(camelcase)
