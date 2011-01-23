""" Repo manifest to OPML

Generates an OPML file for use in things like Google Reader from a repo
manifest.xml file. More information on repo can be found at:
    http://android.git.kernel.org/?p=tools/repo.git;a=summary

Copyright (c) 2011 Adam Carmichael <carneeki@carneeki.net>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


Usage: python repo2opml.py [options]


Options:
    h, --help       display this message
    d, --debug
    m, --manifest=  url or local file, use hyphen (-) for STDIN
    l, --label=     label for Google Reader
    j, --head=      <head /> element for OPML

"""

import urllib
from xml.dom import minidom

_debug = 0
defManifest = 'https://github.com/coolya/android/raw/master/default.xml'

class Manifest:
    """repo manifest to OPML converter"""

    def __init__(self, source=None):
        self.loadManifest(source and source or self.getDefaultSource())

    def loadSource(self, source):
        """load source"""

        usock = urllib.urlopen(source)
        manifest = minidom.parse(usock)
        usock.close()

    def getDefaultSource():
        """return default source"""
        return defManifest

def getRemotes(manifest):
    xRemotes  = manifest.getElementsByTagName('remote')

    for xRemote in xRemotes:
        remotes[xRemote.getAttrValue('name')] = xRemote.getAttrValue('remote')

def getProjects(manifest):
    xProjects = manifest.getElementsByTagName('project')
    projects = {}

    for xProject in xProjects:
        projects[xmlProject.

def usage():
    print __doc__

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hml:d", ["help", "manifest=", "label=", "debug"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-d", "--debug"):
            global _debug
            _debug = 1
        elif opt in ("-m", "--manifest"):
            manifest = arg
        elif opt in ("-l", "--label"):
            opml['label'] = arg
        elif opt in ("j", "--head"):
            opml['head'] = arg

    m = Manifest(manifest,opml)
    print m.output()

foo = """\
<?xml version="1.0" encoding="UTF-8"?>
<opml version="1.0">
    <head>
        <title>Adam subscriptions in Google Reader</title>
    </head>
    <body>
        <outline title="CM-repo" text="CM-repo">
            <outline
                text="$THE_PATH"
                title="$THE_PATH"
                type="rss"
<?php if($THE_PATH == "android.git.kernel.org") { ?>
                xmlUrl="$THE_REMOTE/?p=$THE_PATH.git;a=atom" htmlUrl="$THE_REMOTE/?p=$THE_PATH.git;a=summary"/>
<?php } // android.git.kernel.org
      if($THE_PATH == "github.com") { ?>
                xmlUrl="$THE_REMOTE/?p=$THE_PATH/commits/gingerbread.atom" htmlUrl="$THE_REMOTE/?p=$THE_PATH/commits/gingerbread"/>
<?php } ?>
          </outline>
    </body>
</opml>
"""