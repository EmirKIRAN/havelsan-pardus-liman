#!/bin/bash
sudo apt list | wc -l > count.log
cat ./count.log
