# How to update Anaconda

## Updating conda and Anaconda

The [Anaconda manual](https://docs.anaconda.com/free/anaconda/install/update-version/#:~:text=Updating%20all%20packages%20in%20the,using%20the%20--all%20tag.&text=Using%20the%20--all%20flag,the%20latest%20version%2C%20if%20possible.) have a good page on how to do it.

Basically
```
# Update the conda package manager to the latest version in your base environment
conda update -n base conda
# Use conda to update Anaconda to the latest version in your base environment
conda update -n base anaconda
```

