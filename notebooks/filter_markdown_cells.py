!pip install nbformat

import nbformat

def filter_markdown_cells(notebook_path):
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
        markdown_cells = [cell for cell in nb.cells if cell.cell_type == 'markdown']
        return markdown_cells

def write_markdown_cells_to_file(markdown_cells, output_file):
    with open(output_file, 'w') as f:
        for cell in markdown_cells:
            f.write(''.join(cell.source))
            f.write('\n\n')  # Add two newlines between cells

def filter_and_write_markdown(notebook_path, output_file):
    markdown_cells = filter_markdown_cells(notebook_path)
    write_markdown_cells_to_file(markdown_cells, output_file)

filter_and_write_markdown('filter_markdown_cells.ipynb', 'filter_markdown_cells.md')

from upload_notebook import upload_notebook_to_github

upload_notebook_to_github('filter_markdown_cells.ipynb')
upload_notebook_to_github('filter_markdown_cells.md')

