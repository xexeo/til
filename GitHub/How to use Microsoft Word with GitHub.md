# How to use Microsoft Word with GitHub

* install pandoc (https://pandoc.org/)

* Create a file .gitattributes in the root folder of the git project

```
# .gitattributes file in **root folder of your git project**
*.docx diff=pandoc
```

* Change the .gitconfig in your **home folder**, usually is C:\Users\YourName, including the following lines
```
# .gitconfig file in your home folder
[diff "pandoc"]
  textconv=pandoc --to=markdown
  prompt = false
[alias]
  wdiff = diff --word-diff=color --unified=1
```

Works like magic, you can see the diffs between (text in) word files.

It does not work with Powerpoint, pandoc can´t read .pptx files.

There are other solutions for Excel files.

[Long version by Martin Fenner, since 2014](https://blog.martinfenner.org/2014/08/25/using-microsoft-word-with-git/)
and I never knew about it. This link was dead the last time I tried.

It seems that [this text](https://blog.front-matter.io/posts/using-microsoft-word-with-git/) explain it more.
