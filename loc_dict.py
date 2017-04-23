# -*- coding: utf-8 -*-
"""Locations dictionary to use as a source for creating loc navigation.

This original locations dict should be used as a source for creating
location navigation.
The location names are in the primary language of the locations. The unique
key for the location is an ascii letters string. English names for the
locations are transliterated according to rus2lat dict rules.

"""
from dalnevost.dalnevostfedok import dalnevostfedok
from juzhnyi.juzhnyifedok import juzhnyifedok
from privolzhskij.privolzhskijfedok import privolzhskijfedok
from severokavkazskij.severokavkazskijfedok import severokavkazskijfedok
from severozapadnyj.severozapadnyjfedok import severozapadnyjfedok
from sibirskij.sibirskijfedok import sibirskijfedok
from tsentralnyj.tsentralnyjfedok import tsentralnyjfedok
from uralskij.uralskijfedok import uralskijfedok


loc_dict = {}
loc_dict.update(dalnevostfedok)
loc_dict.update(juzhnyifedok)
loc_dict.update(privolzhskijfedok)
loc_dict.update(severokavkazskijfedok)
loc_dict.update(severozapadnyjfedok)
loc_dict.update(sibirskijfedok)
loc_dict.update(tsentralnyjfedok)
loc_dict.update(uralskijfedok)


alf = 'абвгдежзийклмнопрстуфхцчшщъыьэюяё'
alfu = alf.decode('utf8')
ALF = 'ЁЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ'
ALFu = ALF.decode('utf8')
rus2lat = {
    'а'.decode('utf8'): u'a',
    'б'.decode('utf8'): u'b',
    'в'.decode('utf8'): u'v',
    'г'.decode('utf8'): u'g',
    'д'.decode('utf8'): u'd',
    'е'.decode('utf8'): u'e',
    'ё'.decode('utf8'): u'e',
    'ж'.decode('utf8'): u'zh',
    'з'.decode('utf8'): u'z',
    'и'.decode('utf8'): u'i',
    'й'.decode('utf8'): u'j',
    'к'.decode('utf8'): u'k',
    'л'.decode('utf8'): u'l',
    'м'.decode('utf8'): u'm',
    'н'.decode('utf8'): u'n',
    'о'.decode('utf8'): u'o',
    'п'.decode('utf8'): u'p',
    'р'.decode('utf8'): u'r',
    'с'.decode('utf8'): u's',
    'т'.decode('utf8'): u't',
    'у'.decode('utf8'): u'u',
    'ф'.decode('utf8'): u'f',
    'х'.decode('utf8'): u'h',
    'ц'.decode('utf8'): u'ts',
    'ч'.decode('utf8'): u'ch',
    'ш'.decode('utf8'): u'sh',
    'щ'.decode('utf8'): u'sch',
    'ъ'.decode('utf8'): u"",
    'ы'.decode('utf8'): u'y',
    'ь'.decode('utf8'): u"",
    'э'.decode('utf8'): u'e',
    'ю'.decode('utf8'): u'ju',
    'я'.decode('utf8'): u'ja',
    'А'.decode('utf8'): u'A',
    'Б'.decode('utf8'): u'B',
    'В'.decode('utf8'): u'V',
    'Г'.decode('utf8'): u'G',
    'Д'.decode('utf8'): u'D',
    'Е'.decode('utf8'): u'E',
    'Ё'.decode('utf8'): u'E',
    'Ж'.decode('utf8'): u'ZH',
    'З'.decode('utf8'): u'Z',
    'И'.decode('utf8'): u'I',
    'Й'.decode('utf8'): u'J',
    'К'.decode('utf8'): u'K',
    'Л'.decode('utf8'): u'L',
    'М'.decode('utf8'): u'M',
    'Н'.decode('utf8'): u'N',
    'О'.decode('utf8'): u'O',
    'П'.decode('utf8'): u'P',
    'Р'.decode('utf8'): u'R',
    'С'.decode('utf8'): u'S',
    'Т'.decode('utf8'): u'T',
    'У'.decode('utf8'): u'U',
    'Ф'.decode('utf8'): u'F',
    'Х'.decode('utf8'): u'H',
    'Ц'.decode('utf8'): u'TS',
    'Ч'.decode('utf8'): u'CH',
    'Ш'.decode('utf8'): u'SH',
    'Щ'.decode('utf8'): u'SCH',
    'Ъ'.decode('utf8'): u"",
    'Ы'.decode('utf8'): u'Y',
    'Ь'.decode('utf8'): u"",
    'Э'.decode('utf8'): u'E',
    'Ю'.decode('utf8'): u'JU',
    'Я'.decode('utf8'): u'JA',
}


def translit(s, dic=rus2lat):
        t = ''
        for c in s:
                if c in dic:
                        t += dic[c]
                else:
                        t += c
        return t
