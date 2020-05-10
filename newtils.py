import os
from glob import glob



MD_FILE_LIST = (y for x in os.walk(".")
                for y in glob(os.path.join(x[0], '*.md')))

with open('README.md', 'w') as f:
    text = []
    with open('til.md','r') as g:
        for line in g:
            f.write(line)
    for m_file in MD_FILE_LIST:
        levels = m_file.count(os.sep)
        if levels < 3:
            text.append( ' * ' + '#' * levels + ' [%s](./%s)\n' % (
                                 m_file.split(os.sep)[-1].replace('.md', '').replace('_',' '),
                                 m_file.replace(os.sep,'/')))
        else:
            text.append('%s[%s](./%s)\n' % (m_file.count(os.sep)*' ' + '- ',
                     m_file.split(os.sep)[-1].replace('.md', '').replace('_',' '),
                     m_file.replace(os.sep, '/')))
    text[0] = "# Index\n"
    f.writelines(text)
