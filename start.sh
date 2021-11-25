#!/bin/bash
if [ $# -eq 2 ]
then
	cd generator
	python3 choreography.py

	cd ..
	python2 main.py $1 $2
else
  echo 'parameter not valid'
fi