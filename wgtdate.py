#!/usr/bin/python
from datetime import date, timedelta


def wgt_begin(year):
    return __easter(year) + timedelta(days=48)


def wgt_end(year):
    return __easter(year) + timedelta(days=51)


def wgt_count(year):
    return (year - 1991)


def __easter(year):
    a = year % 19
    b, c = divmod(year, 100)
    d, e = divmod(b, 4)
    f = (b + 8) / 25
    g = (b - f + 1) / 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) / 451
    month, day = divmod(h + l - 7 * m + 114, 31)
    return date(year, month, day)
