# How to remove committed files from Git version control

1. Create a .gitignore file, if you haven't already.
1. Edit .gitignore to match the file/folder you want to ignore.
1. Execute the following command: git rm --cached path/to/file.
1.1. --cached will keep the file in your local folder
1. Verify that these files are being deleted from version control using git status.
1. Push the changes to the repository.

