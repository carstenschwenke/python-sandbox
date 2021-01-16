#!/usr/bin/env python
import datetime
import ephem # to install, type$ pip install pyephem

def calculate_time(d, m, y, lat, long, is_rise, utc_time):
    o = ephem.Observer()
    o.lat, o.long, o.date = lat, long, datetime.date(y, m, d)
    sun = ephem.Sun(o)
    next_event = o.next_rising if is_rise else o.next_setting
    return ephem.Date(next_event(sun, start=o.date) + utc_time*ephem.hour
                      ).datetime().strftime('%H:%M')


for town, kwarg in { "Fredericton": dict(d=3, m=3, y=2010,
                                         lat='45.959045', long='-66.640509',
                                         is_rise=True,
                                         utc_time=20),

                     "Beijing": dict(d=29, m=3, y=2010,
                                     lat='39:55', long='116:23',
                                     is_rise=True,
                                     utc_time=+8),

                     "Berlin": dict(d=12, m=12, y=2019,
                                    lat='52:30:2', long='13:23:56',
                                    is_rise=False,
                                    utc_time=+1) ,

                     "Moscow": dict(d=4, m=4, y=2010,
                                    lat='55.753975', long='37.625427',
                                    is_rise=True,
                                    utc_time=4) }.items():
    print(town, calculate_time(**kwarg))



