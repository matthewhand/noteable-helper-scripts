# Noteable Helper Scripts

This repository contains helper scripts for working with Noteable notebooks. The scripts are designed to automate common tasks such as uploading notebooks to GitHub and filtering Python cells from a notebook.

## Files

The following files are included in this repository:

- [upload_notebook.ipynb](https://app.noteable.io/f/0ef0f288-af3d-43c6-9b04-0ec796599f91/): This notebook contains a script to upload a notebook to a GitHub repository.
- [filter_python_cells.ipynb](https://app.noteable.io/f/2f96c7aa-442d-4335-817b-2af7b985d58a/): This notebook contains a script to filter Python cells from a notebook and write them to a `.py` file.
- [notebook_to_script.ipynb](https://app.noteable.io/f/bbfa4ba5-cf61-48be-88bb-fd2193806178/): This notebook contains a script to convert a notebook to a Python script.

## Usage

To use these scripts, you will need to update them to use the appropriate references for your specific project needs. For example, you will need to update the GitHub repository in the `upload_notebook.ipynb` script to point to your own GitHub repository.

Once you have updated the scripts, you can run them in a Noteable notebook to perform the desired tasks.


```
upload_notebook_to_github('README.ipynb')
```


```
from upload_notebook import upload_notebook_to_github

upload_notebook_to_github('README.ipynb')
```


```
!pip install PyGithub
```


```
from upload_notebook import upload_notebook_to_github

upload_notebook_to_github('README.ipynb')
```
