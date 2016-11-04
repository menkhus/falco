#!/usr/bin/env python
about = """
    copy the nvd datafiles from NIST and then use the
    nvd2sqlite3 program to load them into /usr/local/falco/db/cvedb

    this is a python app which implements control of shell
    commands.  depends on curl, gunzip and rm to implement
    the features.

    Mark Menkhus, June 2016
"""
import datetime
import subprocess
import sys
import os
import tempfile

__version__ = '0.1'

# start year is the year where we want to get the
# beginning of the NVD data
start_year = 2002

# valid year for whenever this is executed
current_year = datetime.date.today().year


def useage():
    prog = sys.argv[0]
    progname = os.path.basename(prog)
    print "%s: %s [-a get all nvd files for database]" % (prog, progname)
    print about
    sys.exit()


def get_nvdfile_to_db(nvdfilename=''):
    """ pull a file from the nist site, unzip it and
    store in the /usr/local/falco/db/cvedb database
    """
    url = r'https://nvd.nist.gov/feeds/xml/cve/' + nvdfilename
    tmp = '/tmp'
    output = tmp + '/' + nvdfilename
    output = tempfile.mkstemp(suffix='.gz', dir=tmp)[1]
    # use curl to copy the file
    cmd = 'curl -s -o ' + output + " " + url
    print "cmd: %s" % (cmd,)
    print "file: %s\nurl: %s\ncmd: %s" % (nvdfilename, url, cmd)
    cmd = cmd.split()
    try:
        subprocess.call(cmd)
        # uncompress the downloaded file
        subprocess.call(['gunzip', output])
        nvdfilename = output.strip(r'.gz^')
        cmd = "load.sh " + nvdfilename
        print "cmd: %s" % (cmd,)
        cmd = cmd.split()
        subprocess.call(cmd)
        cmd = "rm " + nvdfilename
        print "cmd: %s" % (cmd,)
        subprocess.call(cmd.split())
        print
        return True
    except Exception, oops:
        print "nvdloader.py: get_nvd_to_db: %s\ncmd: %s" % (
            oops, cmd)
        return False


def main():
    """ load the nvd database from XML representation downloaded
    from nist.nvd.gov.
    default load only the recent updates and the modified
    or if -a download the files by year from 2002 until the most
    recent year. Then download the most recent updated and
    then finally load the modified ones

    """
    if len(sys.argv) == 1:
        get_nvdfile_to_db(r'nvdcve-2.0-Recent.xml.gz')
        get_nvdfile_to_db(r'nvdcve-2.0-Modified.xml.gz')
    elif '-a' in sys.argv:
        for year in range(start_year, current_year+1):
            filename = r'nvdcve-2.0-' + str(year) + r'.xml.gz'
            get_nvdfile_to_db(filename)
        get_nvdfile_to_db(r'nvdcve-2.0-Recent.xml.gz')
        get_nvdfile_to_db(r'nvdcve-2.0-Modified.xml.gz')
    else:
        useage
    sys.exit()


if __name__ == "__main__":
        main()
