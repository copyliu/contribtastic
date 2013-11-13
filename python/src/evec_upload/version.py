#    EVE-Central.com Contribtastic
#    Copyright (C) 2005-2012 StackFoundry LLC
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License (in file COPYING) for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.


import os
import re
import exceptions
import sys
import urllib

ProgramVersion = 2013
ProgramVersionNice = "2.1.3"
CheckVersion = 2013



class ProtocolVersionMismatch(exceptions.Exception):
    pass


def check_protocol():
    pc = urllib.urlopen("http://www.ceve-market.org/app/protocol_version.txt")
    version = pc.readline().strip()
    pc.close()
    if version != "1":
        raise ProtocolVersionMismatch


def check_client():
    global ProgramVersion
    cv = urllib.urlopen("http://www.ceve-market.org/app/client_version.txt")
    fversion = cv.readline().strip()
    version = cv.readline().strip()
    version = int(version)
    cv.close()
    if version > ProgramVersion:
        return fversion
    else:
        return True
