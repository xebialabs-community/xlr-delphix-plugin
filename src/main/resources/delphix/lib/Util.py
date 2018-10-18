from DlpxException import DlpxException

"""
Module that provides utility functions for tasks.
"""
def form_bookmark_path(template_name, container_name, branch_name, bookmark_name):
    if container_name:
        return "/%s/%s/%s/%s" % (template_name, container_name, branch_name, bookmark_name)
    else:
        return "/%s/%s" % (template_name, bookmark_name)

def form_path(*args):
    result = ''
    for arg in args:
        result = result + '/' + arg

    return result

def split_bookmark_path(bookmark_path):
    """
    object paths are of the form:
    /<template_name>/<container_name>/<branch_name>/<bookmark_name> for container bookmarks
    or
    /<template_name>/<bookmark_name> for template bookmarks
    """
    if bookmark_path[0] != '/':
        raise DlpxException("'%s' is not a valid absolute path. It must start with '/'" % bookmark_path)

    path_el = bookmark_path[1:].split('/')

    result = {}

    if len(path_el) > 2:
        result['template_name']  = path_el[0]
        result['container_name'] = path_el[1]
        result['branch_name']    = path_el[2]
        result['bookmark_name']  = path_el[3]
    else:
        result['template_name']  = path_el[0]
        result['container_name'] = None
        result['branch_name']    = None
        result['bookmark_name']  = path_el[1]

    return(result)

def split_path(obj_path):
    """
    split an object path into constituent parts, up to container bookmarks:
    <template_name>/<container_name>/<branch_name>/<bookmark_name>
    shorter path returns None for missing elements
    """
    if obj_path[0] != '/':
        raise DlpxException("'%s' is not a valid absolute path. It must start with '/'" % obj_path)

    path_el = obj_path[1:].split('/')

    result = {}

    result['template_name']  = path_el[0] if len(path_el) > 0 else None
    result['container_name'] = path_el[1] if len(path_el) > 1 else None
    result['branch_name']    = path_el[2] if len(path_el) > 2 else None
    result['bookmark_name']  = path_el[3] if len(path_el) > 3 else None

    return result