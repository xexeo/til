# How to exclude files from GitHub releases

GitHub uses the command ```git archive``` to create the releases.

You can control what goes in a archive using the ```.gitattributes``` file.

One of the instructions you can put there is ```export-ignore```.

This is an example:

```
Tabelas export-ignore
*.tex export-ignore
README.md export-ignore
```

In the above example, ```Tabelas``` is a sub-folder,
 ``*.tex``` refers to all TeX files, and ```README.md```
refers to a specific file. All of them will be completely ignored when
the directory where this ```.gitattributes``` is archived. Therefore,
you have this file in the main folder of your repo, only files that
do not fit those patterns will be archived, i.e., put in the release.

As far as I know, .getattributes work in sub-folders, and are
processed recursively.

More about [gitattributes](https://git-scm.com/docs/gitattributes)
