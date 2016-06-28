#!/usr/bin/env python
"""
    copy the nvd datafiles from NIST and then use the
    nvd2sqlite3 program to load them into /var/db/cvedb

    this is a python app which implements control of shell
    commands.  depends on curl, gunzip and rm to implement
    the features.

    Mark Menkhus, June 2016
"""
import datetime
import subprocess
import sys

__version__ = '0.1'

# start year is the year where we want to get the
# beginning of the NVD data
start_year = 2002

# valid year for whenever this is executed
current_year = datetime.date.today().year


def get_nvdfile_to_db(nvdfilename=''):
    """ pull a file from the nist site, unzip it an
    load it into the /var/db/cvedb  database
    """
    url = r'https://nvd.nist.gov/feeds/xml/cve/' + nvdfilename
    # use curl to copy the file
    cmd = 'curl -s -o ' + nvdfilename + " " + url
    print "cmd: %s" % (cmd,)
    # print "file: %s\nurl: %s\ncmd: %s" % (nvdfilename, url, cmd)
    cmd = cmd.split()
    try:
        subprocess.call(cmd)
        # uncompress the downloaded file
        subprocess.call(['gunzip', nvdfilename])
        nvdfilename = nvdfilename.strip('.gz')
        cmd = "./load.sh " + nvdfilename
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
        download the files by year form 2002 until the most
        recent year.

        download the most recent updated and then the modified ones

    """
    get_nvdfile_to_db(r'nvdcve-2.0-Recent.xml.gz')
    get_nvdfile_to_db(r'nvdcve-2.0-Modified.xml.gz')

    for year in range(start_year, current_year+1):
        filename = r'nvdcve-2.0-' + str(year) + r'.xml.gz'
        get_nvdfile_to_db(filename)
    sys.exit(0)


if __name__ == "__main__":
        main()
