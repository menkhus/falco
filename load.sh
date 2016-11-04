#!/bin/bash
cat $1 | nvd2sqlite3 -d /usr/local/falco/db/cvedb
