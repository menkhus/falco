#!/bin/bash
cat $1 | nvd2sqlite3 -d $2
