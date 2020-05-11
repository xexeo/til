import os
from glob import glob
import pathlib
import sys

MD_FILE_LIST = (y for y in os.walk("."))

for m_file in MD_FILE_LIST:
  print(m_file[0].replace(os.sep,"/").replace("/logs/refs/","Ameixa"))
