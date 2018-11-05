import datetime
import numpy as np
import os
import pandas as pd
from pathlib import Path


def get_data(GitHubPath):
    """Gets data for example table
    """

    df = pd.read_excel(GitHubPath/'GitHub-Pages-Example/example-data.xlsx')

    return df


def markdown():
    """Converts the markdown file into html
    """
    import markdown2
    from markdown2 import markdown_path
    with open('body.md') as f:
        md = [x.strip('') for x in f]
    
    mdString = ''.join(md)
    content = markdown2.markdown(mdString, 
                                extras=['footnotes','smarty-pants','cuddled-lists','target-blank-links',
                                        'tables','header-ids','break-on-newline', 'header-ids',
                                        'fenced-code-blocks'])
    doc = [content]
    # doc = head+content+foot

    with open('html/body/body.html', mode='wt', encoding='utf-8') as myfile:
        for lines in doc:
            myfile.write(''.join(lines))
            myfile.write('\n')


def update_data(homePath, GitHubPath):

    # example table data
    df = get_data(GitHubPath)
    savePath = str(GitHubPath)+'/GitHub-Pages-Example/scripts/html/df/df.txt'
    df.to_html(open(savePath, 'w'), index=False, table_id='demo')

    # body markdown
    markdown()


def insert_html(htmlOriginal, htmlAdd, insertionPoint):
    """Inserts HTML from one file (htmlAdd) into another (htmlOriginal) at insertionPoint
    """
    import fileinput

    with open(htmlAdd) as f:
        head = [x.strip('\n') for x in f]
    head = [x.strip() for x in head] 
    for line in fileinput.input(htmlOriginal, inplace=1):
        if line.startswith(insertionPoint):
            for lineHead in range(len(head)):
                print(head[lineHead])
        else:
            print(line)


def copy_file(src, dst):
    """Copy file (src) to dst.
    """
    import shutil
    src = str(src)
    dst = str(dst)
    shutil.copy(src, dst)


def build():
    """Build the site's index.html
    """
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    fname = '../index.html'

    copy_file(src='_template.html', dst='../index.html')
    
    # add body
    htmlAdd = 'html/body/body.html'
    print(htmlAdd)
    insert_html(htmlOriginal=fname, htmlAdd=htmlAdd, insertionPoint='    <!-- INSERT BODY -->')

    # add table
    htmlAdd = 'html/df/df.txt'
    insert_html(htmlOriginal=fname, htmlAdd=htmlAdd, insertionPoint='<p>XXX-INSERT TABLE HERE-XXX</p>')
    # insert_html(htmlOriginal=fname, htmlAdd=htmlAdd, insertionPoint='    <!-- INSERT TABLE -->')

    # add filter table
    htmlAdd = 'html/tablefilter.html'
    insert_html(htmlOriginal=fname, htmlAdd=htmlAdd, insertionPoint='<!-- ADD TABLEFILTER SCRIPT -->')

    # replace text
    with open(fname) as f:
        head = [x.strip('\n') for x in f]
    for line in range(len(head)):
        head[line] = head[line].replace('#DATE#',date)
    with open(fname, mode='wt', encoding='utf-8') as myfile:
        for line in head:
            if len(line)>0:
                myfile.write(''.join(line))
                myfile.write('\n') 


def main():
    # get paths
    homePath = Path.cwd().home()
    for parent in Path.cwd().parents:
        if str(parent)[-6:]=='GitHub':
            GitHubPath = parent

    # update data
    print('Updating data')
    update_data(homePath, GitHubPath)

    # build site
    print('Updating HTML')
    build()
    print('Done.\n')


if __name__ == "__main__":
    main()