import os
from glob import glob
import git
import pathlib
import sys

directory_levels_in_git_run = 5
markdown_max = 6

# this is where I am now, in Github space
root = str(pathlib.Path(__file__).parent.resolve())

# there are <directory_levels_in_git_run> extra leves of folders
# in running environment
# also, the size of the fila_dirs counts how many empty diretories
# in the hierarchy, while if there is only one, nothing to change
# finally Markdown has only <markdown_max> levels deep (hope never arrives there)
def calculate_level(levels,fila_dirs):
    return min(levels-directory_levels_in_git_run-len(fila_dirs)+1,markdown_max)

# must eliminate spaces and put space codes in url to work in markdown
def url_maker(path,file):
    return path.replace(" ","%20")+"/"+file.replace(os.sep, '/').replace(" "
                ,"%20")

# in a list of file names, seek one with .md in name
def find_sub_in_list(a_list,a_sub_string):
    return any(a_sub_string in s for s in a_list)
#    for s in a_list:
#        if a_sub_string in s:
#            return True
#    return False

def fix_path(apath):
    the_temp_path = str(apath.replace(os.sep,'/'))
    the_path = the_temp_path.replace("/home/runner/work/til/til",'')
    return(the_path)


# this gives a list of 3-plets:
# first is path (almost a string) with directory - always present
# second is list of subdirs - can be empty at leaves
# third is a lista of files - can be empty anywhere
# they come in some sequence,       it is system dependent
# but works DEEP FIRST (At least, until now)
# If not DEEP FIRST, program will break
MD_FILE_LIST = (y for y in os.walk(root))

with open(root+'/README.md', 'w') as f:
    # save everything in memory to flush in the end
    # saves times? This is cargo cult from previous author
    text = []
    with open(root+'/til.md','r') as g:
        for line in g:
            f.write(line)
    # keep a list as a queue to save empty folders names
    # need deep first to work
    fila_dirs = []
    for m_file in MD_FILE_LIST:
        # processa o diretório
            # need to know how many levels
            directory = m_file[0].split(os.sep)
            levels = len(directory)
            last = directory[-1]
            fila_dirs.append(last) # here needs deep first

            # need the files
            files = m_file[2]


            the_path = fix_path(m_file[0])


            # we check for one .md file, but can have other files
            # if there is one, must process the list
            if files and find_sub_in_list(files,".md"):
                # here DEEP FIRST is important, will empty queue
                # if there is any file to put in index
                while fila_dirs:
                    text.append('#' * calculate_level(levels,fila_dirs)
                                     +' %s\n' % fila_dirs.pop(0))
                # put all .md files in Index
                for file in files:
                    #text.append("The path is: "+the_path+"\n")
                    if ".md" in file:
                        text.append('- [%s](./%s)\n' %
                                ( file.replace('.md', ''),
                                url_maker(the_path,file)
                                )
                            )
            elif len(m_file[1])==0:
                fila_dirs = [] # if no more folders, kills queue

    text[0] = "# Index\n" # avoid .til to appear and put index
    f.writelines(text)
