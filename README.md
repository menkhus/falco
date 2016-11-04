Falco: 3rd party code security intelligence for software maintainers
==================================================

What is falco?
--------------
Falco is a simple tool to search the NIST NVD and report latent security bugs in 3rd party software packages in your projects. By placing falco in your build or QA process, you can be alerted when new security defects are reported.  You could make falco part of your architectural review process as you evaluate component choices.

Falco Dependencies
------------------
Falco depends on the nvdsqlite3, a sqlite loader of the NIST NVD
vulnerability database. You must pip install nvdsqlite3 and pystache. Then update the cvedb database and then point falco at runtime at the up-to-date database in order to have an effective vulnerability intelligence feature in your software workflow.

Thanks and shout outs:
----------------------
Jan Schaumann, twitter for https://github.com/jschauma/nvd2sqlite3
NJ Ouchn, vfeed database, awesome tool!

Use this command to install and update the NVD database:
$ ./falco -u

Also use the same update command periodically. The cvedb database must be updated periodically in order to implement the notion that you are getting current threat knowledge.

Setup for first use from the falco directory:  

```bash
$ ./falco -u
```  

If you find falco useful, please give a shoutout to us, and the great folks who build and maintain toolswatch cve database that helped use get the project started.

No free lunch
-------------
Users of falco are responsible for making sure the package names, and versions supplied to falco are current with the project being evaluated. There is no sophistication built into falco to survey your code for 3rd party dependencies.There are commercial products which can do this and so much more. Falco users must obtain and manage their own configuration management data for their project.

Recently, Jeremy Long, of OWASP dependency-check gave me a heads up regarding other FOSS projects that also provide 3rd party code dependency security checks. See the list below for some other 3rd party code dependency check apps.

Open source 3rd party software dependency apps
----------------------------------------------
* Victims - https://github.com/victims
* OWASP dependency-check - https://jeremylong.github.io/DependencyCheck/
* JavaScript retire.js - https://github.com/victims/victims-enforcer
* fossology - http://www.fossology.org/projects/fossology (license checking)

Commercial products that do dependency checks
---------------------------------------------
* Appcheck from codenomicon - http://appcheck.codenomicon.com/help/faq/
* Palamida - http://www.palamida.com/
* Blackduck - https://www.blackducksoftware.com/

Why falco
---------
We wrote the tool because (at the time we looked) there were no accessible tools for developers and project maintainers to easily find known security vulnerabilities in software they use as part of a project.  Falco is bare-bones simple, and implements a basic software security check mandated by many security maturity models such as the one in OWASP: https://www.owasp.org/index.php/Top_10_2013-A9-Using_Components_with_Known_Vulnerabilities, OpenSAMM - http://www.opensamm.org/, or BSIMM - http://www.bsimm.com/online/governance/cp/

Falco is not a code scanner
---------------------------
Falco does not test the software, it simply looks to see that the package and version you tell it are in a vulnerability database.  If a package and version are in the vulnerability database, you could have a vulnerability in software you depend upon. You need to respond to by validating that vulnerability assertion, and then update the package as needed.  Other ways to discover known exiting vulnerabilities are through code scanning tools (mentioned above) network security scanners like OpenVAS or Nessus  (often used by commercial customers) and using code analysis tools like HP Fortify or Coverity.

Do 3rd party code threat intelligence
-------------------------------------
If you are developing a security lifecycle for your project, then managing 3rd party code security bugs is just a small part of a very baseline behavior. We wish you luck and hope that falco helps in your journey.

Mark Menkhus, RedCup working group
menkhus@icloud.com

July 11, 2014

All rights reserved.

(c) Copyright 2015 Falconry Concepts LLC.

License
-------
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Falco help
----------
usage: falco [-h] [-b] [-c] [-C [CVE]] [-d [CVEDB_DATABASE]]
             [-f [PACKAGELISTFILE]] [-i [ITEMS_REPORTED]] [-n [PACKAGE_NAME]]
             [-o [OUTPUTFILE]] [-t [TYPE]] [-u] [-v [PACKAGE_VERSION]] [-V]

Checks command line or, a file list of software programs for known security
defects documented in the National Vulnerability Database. Matches a project
name and version name to CPE URIs in the NVD database. Uses the Copyright
2013, nvd2sqlite3 app.

optional arguments:

usage: falco [-h] [-b] [-c] [-C [CVE]] [-d [CVEDB_DATABASE]]
             [-f [PACKAGELISTFILE]] [-i [ITEMS_REPORTED]] [-n [PACKAGE_NAME]]
             [-o [OUTPUTFILE]] [-t [TYPE]] [-m [MINIMUM_DATE]] [-u]
             [-v [PACKAGE_VERSION]] [-V]

Checks command line or, a file list of software programs for known security
defects documented in the National Vulnerability Database. Matches a project
name and version name to CPE URIs in the NVD database. Uses the Copyright
2013, nvd2sqlite3 app, thanks to: Jan Schaumann for
https://github.com/jschauma/nvd2sqlite3

optional arguments:
  -h, --help            show this help message and exit
  -b, --build_environment
                        for use in build environments, return fail if items
                        found
  -c, --config          update database and setup for use. Do this after
                        manually downloading a new database
  -C [CVE], --CVE [CVE]
                        display a CVE entry
  -d [CVEDB_DATABASE], --cvedb_database [CVEDB_DATABASE]
                        location of the cvedb sqlite database
  -f [PACKAGELISTFILE], --packagelistfile [PACKAGELISTFILE]
                        file where the list of packages to evaluate is stored
  -i [ITEMS_REPORTED], --items_reported [ITEMS_REPORTED]
                        number of items reported for NVD/CVE matches
  -n [PACKAGE_NAME], --package_name [PACKAGE_NAME]
                        package name to search for
  -o [OUTPUTFILE], --outputfile [OUTPUTFILE]
                        name of output file
  -t [TYPE], --type [TYPE]
                        format of output, options are text, html, json
  -m [MINIMUM_DATE], --minimum_date [MINIMUM_DATE]
                        the minimum date we look for in the database for
                        matches, default is the beginning of the data.format
                        is like 2003-11-17
  -u, --update          download database. Do this about once a week
  -v [PACKAGE_VERSION], --package_version [PACKAGE_VERSION]
                        package version to look for
  -V, --Version         report the version of falco and exit

Usage Examples
-----------------------
Assumes cvedb is in the /usr/local/bin/falco/db directory  

### Example 1, check a package named 'python' version '2.7.3' for vulnerabilities in the NVD database ###

```sh
./falco.py -n http_server -m 2001-01-01
```    
*** Potential security defect found in http_server:
CVE: CVE-2012-5955
CVSS Score: 10.0
Vulnerable software list, CPE id: [u'cpe:/a:ibm:http_server:5.3', u'cpe:/a:ibm:websphere_application_server:-:-:~~~z%2fos~~']
Published on: 2012-12-20T07:02:19.937-05:00
Summary Description: Unspecified vulnerability in the IBM HTTP Server component 5.3 in IBM WebSphere Application Server (WAS) for z/OS allows remote attackers to execute arbitrary commands via unknown vectors.

### Example 2, using falco in build situations ###

Assume the feed database is in the /var/db subdirectory. Check a package named 'python' version '2.7.3' for vulnerabilities in the NVD database and if any are found, return a non zero return value.  Placing this in a makefile will cause make to exit when a vulnerability matches.  

```bash
$ ./falco.py -n python -v 2.7.3 -m 2001-01-01 -b -o falcolog
$ echo $?  
1  
$  
```  

### Example 3, falco in a makefile, using the -b (break the build) flag ###

#### Makefile: ####
\# this will FAIL make because this version 1.14.7 bash is found in the NVD  
\# database.  
\# Solution is twofold: to update bash to most recent code, and  
\# to change the # make entry to reflect that new version number:  
bash.build.out:  
    ./falco.py -b -n bash  -v 1.14.7 -d /var/db/cvedb > bash.build.out  
clean:  
    rm bash.build.out  

#### Execution ####

```bash
$ make  
./falco.py -b -n bash  -v 1.14.7 -d /var/db/cvedb -o bash.build.out  
make: *** [bash.build.out] Error 1  
```  
#### Explanation ####
 -b cause falco to return fail if any there are CVE findings returned from searching NVD for the package and version.

#### Suggested action ####
File a bug in the bug tracker, change the makefile, remove -b, and when the bug is fixed, update the makefile again to reflect the latest package number and reinstate the -b   

Dependencies
------------
1) update the cvedb for initial use, using nvdloader -a 

2) Note it would be a good idea to put this "falco -u" in a cron job, since falco counts on using updated NVD data to see when new vulnerabilities exist. This database is updated every few weeks.

bug reports
-----------
send bug reports to menkhus@icloud.com  
