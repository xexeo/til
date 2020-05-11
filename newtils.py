import os
from glob import glob
import git
import pathlib
import sys

root = str(pathlib.Path(__file__).parent.resolve())


MD_FILE_LIST = (y for y in os.walk(root))

with open(root+'/README.md', 'w') as f:
    text = [""]
    with open(root+'/til.md','r') as g:
        for line in g:
            f.write(line)
    for m_file in MD_FILE_LIST:
        # processa o diretório
            directory = m_file[0].split(os.sep)
            files = m_file[2]
            levels = len(directory)
            last = directory[-1]
            if files and files[0].find(".md")!=-1:
                print(last,levels)
                text.append(' * '+'#' * levels+' %s\n' % last )
                for file in files:
                    text.append('- [%s](./%s)\n' %
                        ( file.replace('.md', '').replace('_',' '),
                          m_file[0].replace(os.sep, '/')[2:]+"/"+file.replace(os.sep, '/')
                        )
                    )

    text[0] = "# Index\n"
    f.writelines(text)
