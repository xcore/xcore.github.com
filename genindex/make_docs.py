#!/usr/bin/python
from github2.client import Github
import jinja2
import subprocess
import urllib
import urllib2
import re
import sys
from optparse import OptionParser

# This is a very rough and ready script to generate an index
# of github repositories

class DummyRepo:
    pass

usage = "usage: %prog [options] username api_token"
optparser = OptionParser(usage=usage)

optparser.add_option("-d","--dummy-run",dest="dummy_run",
                     action="store_true",default=False,
                     help="Run with dummy data")

optparser.add_option("-s","--static-only",dest="static_only",
                     action="store_true",default=False,
                     help="Only generate static pages (not the index)")

(options, args) = optparser.parse_args()

github_api = True

if options.dummy_run:
    github_api = False
    dummy_repo = True

if options.static_only:
    github_api = False
    dummy_repo = False

if github_api:
    username = args[0]
    api_token = args[1]
    github = Github(username=username,api_token=api_token,requests_per_second=1.3)

    repos = github.organizations.repositories("xcore")
    repos = [r for r in repos if not r.private]
elif dummy_repo:
    dummy = DummyRepo()
    dummy.name = "sw_dummy"
    dummy.description = "Dummy Repo"
    repos = [dummy]
else:
    repos = []


excludes = ['Community','xcore.github.com']
repos = [r for r in repos if not r.name in excludes]
#for repo in repos:
#    print "   * - " + repo.name
#    print "     - " + repo.description

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

groups = []
groups.append({'title':'Software Component Repositories', 'regexp':'sc_.*',
               'repos':[]})
groups.append({'title':'Applications and Reference Design Repositories',
               'regexp':'(sw_.*)|(proj_.*)',
               'repos':[]})
groups.append({'title':'Hardware Repositories',
               'regexp':'(hw_.*)|(proj_.*)',
               'repos':[]})
groups.append({'title':'Documentation Repositories',
               'regexp':'doc_.*',
               'repos':[]})
groups.append({'title':'Development Tool Repositories',
               'regexp':'tool_.*',
               'repos':[]})
unmatched_group = {'title':'Misc. Repositories','repos':[]}
repos.sort(key = lambda r: r.name)


#repos = repos[:10]
#repos = [r for r in repos if r.name == 'sw_avb']

def get_commit_date((tag,commit)):
    c = github.commits.show('xcore'+'/'+repo.name, commit)
    return c.committed_date

def get_tag_version(tag):
    if re.match('v\d.*',tag):
        return tag[1:]
    if re.match('version_.*',tag):
        return tag[8:]
    return None

for repo in repos:
    print "Processing %s" % repo.name
    if github_api:
        tags = github.repos.tags('xcore'+'/'+repo.name)
        tag_list = [(t,c) for (t,c) in tags.items() if get_tag_version(t) != None]
        tag_list.sort(key=get_commit_date)
        repo.tags = [{'name':t,'version':get_tag_version(t)} for (t,c) in tag_list[-1:]]
        matched = False
    else:
        repo.tags = [{'name':'v1.4','version':'1.4'}]

    try:
        doc_link = "http://github.xcore.com/%s/index.html" % repo.name
        urllib2.urlopen(doc_link)
        repo.doc_link = '`docs <%s>`_' % doc_link
    except urllib2.HTTPError:
        repo.doc_link = ''

    for group in groups:
        if re.match(group['regexp'], repo.name):
            matched = True
            group['repos'].append(repo)

    if not matched:
        unmatched_group['repos'].append(repo)

groups.append(unmatched_group)

for group in groups:
    group['repos'].sort(key = lambda r: r.name)

if repos != []:
    print "Rendering index"
    template = env.get_template('index.rst')
    template.stream(groups=groups).dump('doc/index.rst')


for repo in repos:
    print "Rendering %s" % repo.name

    template = env.get_template('readme_insert.rst')
    if github_api:
        remote_readme = urllib.urlopen('https://raw.github.com/xcore/%s/master/README.rst'%repo.name,'doc/%s_readme.rst' % repo.name)
    else:
        remote_readme = open('templates/dummy_readme.rst','r')





    pre_title = []
    post_title = []

    line = remote_readme.readline()
    line = re.sub('\<title\>',repo.name,line)
    if line != '': pre_title.append(line)


    done_title = False
    title_underline = ''
    while not done_title:
        line = remote_readme.readline()
        line = re.sub('\<title\>',repo.name,line)
        if line != '':
            pre_title.append(line)
        done_title = (line == '') or (re.match('(---)|(===)|(\.\.\.)',line))

    title_underline = line

    if line != '':
        while True:
            line = remote_readme.readline()
            if line == '':
                break
            post_title.append(line)

    if title_underline == '':
        post_title = pre_title + post_title
        pre_title = [repo.name + '\n','========\n\n']

    f = open('doc/%s_readme.rst'%repo.name,'w')

    for x in pre_title:
        f.write(x)

    insert = template.render(repo=repo)
    f.write(insert)

    title_underline = '<<<<<<<<<<<<<<<<\n'

    f.write('Details:\n')
    f.write(title_underline+'\n\n')

    for x in post_title:
        f.write(x)

    f.close()

    print "Creating master download page"
    template = env.get_template('download.rst')
    template.stream(repo=repo,tag='master',version='master').dump('doc/%s_master_download.rst'%(repo.name))
    for tag in repo.tags:
        print "Creating %s download page" % tag
        template.stream(repo=repo,tag=tag['name'],version=tag['version']).dump('doc/%s_%s_download.rst'%(repo.name,tag['name']))


for x in ['github_howto.rst','github_howto_11_2.rst']:
    template = env.get_template(x)
    template.stream().dump('doc/%s'%x)


subprocess.call('cd doc;make clean;make all',shell=True)

