import os
from glob import glob
import git
import pathlib
import sys

directory_levels_in_git_run = 5
root = str(pathlib.Path(__file__).parent.resolve())

def calculate_level(levels,fila_dirs):
    return min(levels-directory_levels_in_git_run-len(fila_dirs)+1,3)

def url_maker(path,file):
    return path.replace(" ","%20")+"/"+file.replace(os.sep, '/').replace(" "
                ,"%20")

MD_FILE_LIST = (y for y in os.walk(root))

with open(root+'/README.md', 'w') as f:
    text = []
    with open(root+'/til.md','r') as g:
        for line in g:
            f.write(line)
    fila_dirs = []
    for m_file in MD_FILE_LIST:
        # processa o diretório
            directory = m_file[0].split(os.sep)
            files = m_file[2]
            levels = len(directory)
            last = directory[-1]
            fila_dirs.append(last)

            the_temp_path = str(m_file[0].replace(os.sep,'/'))
            #text.append(the_temp_path+"\n")
            the_path = the_temp_path.replace("/home/runner/work/til/til/",'')
            #text.append(the_path+"\n")

            if files and files[0].find(".md")!=-1:
                while fila_dirs:
                    text.append('#' * calculate_level(levels,fila_dirs)
                                     +' %s\n' % fila_dirs.pop(0))
                for file in files:
                    #text.append("The path is: "+the_path+"\n")
                    text.append('- [%s](./%s)\n' %
                        ( file.replace('.md', '').replace('_',' '),
                          url_maker(the_path,file)
                        )
                    )
            elif len(m_file[1])==0:
                fila_dirs = []

    text[0] = "# Index\n"
    f.writelines(text)
