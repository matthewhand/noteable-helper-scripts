# README.md for root folder

This repository contains helper scripts and advice for using the Noteable and Github plugins with ChatGPT. The environment is already prepared with environment variables (also known as SECRETS in the Noteable web UI). One of these is the `GITHUB_TOKEN` which is used to access the Github API.

The helper scripts are Python scripts that are designed to be used within a Noteable Python notebook. They perform various tasks such as uploading files to a Github repository and filtering a notebook based on the type of cells (Python or Markdown).

The advice is provided in the form of Noteable notebooks and is specific to the plugins and tasks that ChatGPT is currently working with. For instance, when using the ChatSshPlug plugin, ChatGPT should be instructed to read the 'advice_chatsshplug.ipynb' notebook. Similarly, when working with the Noteable plugin, the 'advice_noteable.ipynb' notebook should be read.

Before using the helper scripts, they must be updated for the specific project needs. This involves updating the Github repository and other relevant details.

Links:
- [Helper Scripts](https://github.com/matthewhand/noteable-helper-scripts/tree/main/notebooks)
- [Advice](https://github.com/matthewhand/noteable-helper-scripts/tree/main/notebooks/advice)
