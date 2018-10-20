#
# Copyright 2018 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
import json

from delphixpy.web.database import database
from delphixpy.web.selfservice import bookmark
from delphixpy.web.selfservice import branch

from delphix.lib.DelphixSession import DelphixSession
from delphix.lib.GetReferences import find_bookmark_ref
from delphix.lib.GetReferences import find_obj_name
import delphix.lib.Util as Util


class DelphixClient(object):

    def __init__(self, server):
        self.engine = DelphixSession.create(server).server_session


    @staticmethod
    def create_client(http_connection):
        return DelphixClient(http_connection)

    def delphix_listbookmarks(self, variables):
        js_bookmarks = bookmark.get_all(self.engine)

        path = Util.split_path(variables['template_path'])

        result = []
        for js_bookmark in js_bookmarks:
            if js_bookmark.template_name != path['template_name']:
                continue

            add_it = False
            if variables['tag_filter'] is None:
                tag = js_bookmark.tags if js_bookmark.tags else None
                add_it = True
            else:
                for tag in variables['tag_filter']:
                    if tag in js_bookmark.tags:
                        add_it = True
                        break

            if add_it:
                branch_name = find_obj_name(self.engine, branch, js_bookmark.branch)
                key = Util.form_bookmark_path(js_bookmark.template_name, js_bookmark.container_name, branch_name, js_bookmark.name)
                result.append(key)
                print "%s\n" % key

        variables['bookmarks'] = result

    def delphix_deletebookmark(self, variables):
        path = Util.split_bookmark_path(variables['bookmark_path'])

        bookmark_ref = find_bookmark_ref(self.engine, path['template_name'], path['container_name'], path['branch_name'], path['bookmark_name'])
        bookmark.delete(self.engine, bookmark_ref)

        print "Bookmark '%s' deleted" % variables['bookmark_path']

    def delphix_refreshdatabase(self, variables):
        return database.refresh(self.engine, variables['vdb'], None)
