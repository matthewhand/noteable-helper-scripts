#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nbformat

def filter_python_cells(filename):
    # Read the notebook
    with open(filename) as f:
        nb = nbformat.read(f, as_version=4)

    # Filter out the Python cells
    python_cells = [cell for cell in nb.cells if cell.cell_type == 'code']

    # Write the Python cells to a .py file
    with open(filename.replace('.ipynb', '.py'), 'w') as f:
        for cell in python_cells:
            f.write(''.join(cell.source))
            f.write('\n\n')

    print(f'Successfully filtered Python cells from {filename} and wrote them to a .py file.')


# In[ ]:


get_ipython().system('pip install nbformat')

