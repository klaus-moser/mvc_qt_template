#!/bin/bash

echo "Start converting..."

pyuic5 -o ../view_designer.py view_designer.ui

echo "Finished."
