#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import requests
from getpass import getpass
from github import Github

def upload_notebook_to_github(filename):
    # Get GitHub token
    token = os.getenv('GITHUB_TOKEN')
    g = Github(token)

    # Get repo
    user = g.get_user()
    repo = user.get_repo('noteable-helper-scripts')

    # Read file
    with open(filename, 'r') as file:
        content = file.read()

    # Upload to GitHub
    try:
        repo.create_file(f'notebooks/{filename}', 'Upload notebook', content)
        print(f'Successfully uploaded {filename} to GitHub.')
    except:
        contents = repo.get_contents(f'notebooks/{filename}')
        repo.update_file(contents.path, 'Update notebook', content, contents.sha)
        print(f'Successfully updated {filename} on GitHub.')


# In[ ]:


get_ipython().system('pip install PyGithub')

