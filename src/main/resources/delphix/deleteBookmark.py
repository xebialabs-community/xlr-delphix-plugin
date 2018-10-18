#
# Copyright 2018 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

# Deletes a bookmark
#
# :param dlpx_obj: Virtualization Engine session object
# :type dlpx_obj: lib.GetSession.GetSession
# :param bookmark_name: Bookmark to delete
# :type bookmark_name: str

import sys

from delphixpy.web.jetstream import bookmark
from delphixpy import exceptions

from delphix.lib.DelphixSession import DelphixSession
from delphix.lib.GetReferences import find_bookmark_ref
import delphix.lib.Util as Util

engine = DelphixSession.create(server).server_session

path = Util.split_bookmark_path(bookmark_path)

bookmark_ref = find_bookmark_ref(engine, path['template_name'], path['container_name'], path['branch_name'], path['bookmark_name'])

try:
    bookmark.delete(engine, bookmark_ref)
except exceptions.RequestError as e:
    print 'EXCEPTION: [%s] \n' % e.message
    sys.exit(1)

print "Bookmark '%s' deleted" % bookmark_path
sys.exit(0)
