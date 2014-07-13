#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
"""  software_inventory_vulnerability_check search a list of program
package names and versions in the NVD database.

depends on vfeed database, and a package inventory list
depends on list being in name or name:version format, 1 per line

author: Mark Menkhus
menkhus@icloud.com

All rights reserved.

Copyright 2014 Mark Menkhus

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

__version__ = '0.1'
__author__ = 'Mark Menkhus, menkhus@icloud.com'

class packageList():
    """ return a list of packages to get tested.
        input: filename where the content is a packagenames
        one per line, comments with # sign
    """
    def __init__ (self, packageFile='testlist.txt'):
        """ get a file name when object is instantiated
        """
        self.packageFile = packageFile
        self.packageList = []
    def getList (self):
        """ getList is a generator, it gets the data from the file 
            and yields the data as needed
        """
        import re
        try:
            self.packageListInput = open (self.packageFile, 'r').readlines() 
        except Exception, e:
            print "packageList: Exception - %s"%(e,)
            exit(1)
        for each in self.packageListInput:
            if re.search(r'^#', each):
                pass
            else:
                each = each.strip('\n')
                if each != '':
                    self.packageList.append(each)
                    yield each

def package_check(package=''):
    """ Check a package string for existence in the nvd cpe data
        data string is packagename:version
        depends on the vfeed.db database from the vfeed application
    """
    import sqlite3
    feed = '/Users/menkhus/src/vFeed/vFeed-master/vfeed.db'
    #feed = 'vfeed.db'
    conn = sqlite3.connect(feed)
    cursor = conn.cursor()
#   We need to add the CVSS scores
    sql = r"""SELECT DISTINCT c.cveid, n.cvss_base, c.cpeid, n.date_published, n.summary
    FROM nvd_db as n
    JOIN cve_cpe as c
    WHERE c.cpeid
    """
    sql += r' LIKE "%:' + package
# do we want to filter CVSS about 7?
    sql += r'" and c.cveid = n.cveid ORDER BY n.date_published DESC LIMIT 20;'
    data = cursor.execute(sql)
    if data != None:
        data = data.fetchall()
	if len(data) > 0:
            print "*** Potential security defect found in %s ***"%(package,)
            for entry in data:
                print "CVE: %s\nCVSS Score: %s\nCPE id: %s\nPublished on: \
                %s\nSummary Description: %s\n"%(entry[0],entry[1],\
                entry[2],entry[3],entry[4])
                # can I print the CVSS identifier?
                # can I print the CVSS identifier in such a way
                # that it represents a shape?
                # 
                # how can I model the attack surface?  What ports does 
                # this application use?  
                # What would a malicious attack file look like for this 
                # cve / security defect?
                # what does any attack file look like?
            print
        conn.close()
        return data
    else:
        conn.close()
        return None

class checknvd_by_package_package_check():
    """ Check a package string for existence in the nvd cpe data
        data string is 'packagename:version'
        depends on the vfeed.db database from the vfeed application
    """
    def __init__ (self, package='', database='vfeed.db', items=5):
        """ Setup class 
        """
        import sqlite3
        self.package=package 
        self.database = database
        self.items=items
        try:
            self.conn = sqlite3.connect(feed)
            self.cursor = self.conn.cursor()
        except EXCEPTION,e:
            print "checknvd_by_packagename: %s"%(e,)
            exit()

    def get_data():
        #   todo add the CVSS scores
        self.sql = r"""SELECT DISTINCT c.cveid, n.cvss_base, c.cpeid, n.date_published, n.summary
        FROM nvd_db as n
        JOIN cve_cpe as c
        WHERE c.cpeid
        """
        self.sql += r' LIKE "%:' + self.package
        self.sql += r'" and c.cveid = n.cveid ORDER BY n.date_published '
        self.sql += r'DESC LIMIT ' + self.items + ';'
        self.data = cursor.execute(self.sql)
        if self.data != None:
            self.data = self.data.fetchall()
        if len(self.data) > 0:
                print "*** Potential security defect found in %s ***"%(package,)
                for entry in self.data:
                    print "CVE: %s\nCVSS Score: %s\nCPE id: %s\nPublished on: \
                    %s\nSummary Description: %s\n"%(entry[0],entry[1],\
                    entry[2],entry[3],entry[4])
                    # can I print the CVSS identifier?
                    # can I print the CVSS identifier in such a way
                    # that it represents a shape?
                    # 
                    # how can I model the attack surface?  What ports does 
                    # this application use?  
                    # What would a malicious attack file look like for this 
                    # cve / security defect?
                    # what does any attack file look like?
                print
                self.conn.close()
                return self.data
        else:
            self.conn.close()
            return None

def main ():
    """  read a package inventory file in the form package:version
        check the packages in the NVD database, and report to std out
        depends on vfeed database, package.txt file

    """
    #packages = packageList('packages.txt')
    packages = packageList('testlist.txt')
    packages = packages.getList()
    # we need to put command line options
    # database
    # min cvss
    # clipping limit of the number of CVE's
    # age of the CVE's
    # we need to characterize the attack surface, ports program names
    # we need to characterize how to defend against these problems. Besides
    # patching, what else can be done.
    for package in packages:
        print package
        try:
            p = checknvd_by_package package_check(package=package, database='vfeed.db', items=5)
            print p
            #package_check(package)
        except KeyboardInterrupt:
            # quit the application
            exit()

if __name__ == "__main__":
    main()
