#
# Copyright 2018 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

"""
Module that provides lookups of references and names of Delphix objects.
"""

import re

from delphixpy.web.service import time
from delphixpy.exceptions import RequestError
from delphixpy.exceptions import HttpError
from delphixpy.exceptions import JobError
from delphixpy.web import repository
from delphixpy.web import database
from delphixpy.web import source
from delphixpy.web import job
from delphixpy.web import sourceconfig

from delphixpy.web.selfservice import template
from delphixpy.web.selfservice import container
from delphixpy.web.selfservice import branch
from delphixpy.web.selfservice import bookmark

from DlpxException import DlpxException

VERSION = 'v.0.2.0019'

def find_all_objects(engine, f_class):
    """
    Return all objects from a given class
    engine: A Delphix engine session object
    f_class: The objects class. I.E. database or timeflow.
    :return: List of objects
    """

    return_lst = []

    try:
        return f_class.get_all(engine)

    except (JobError, HttpError) as e:
        raise DlpxException('{} Error encountered in {}: {}\n'.format(
            engine.address, f_class, e))


def find_obj_specs(engine, obj_lst):
    """
    Function to find objects for replication
    engine: Delphix Virtualization session object
    obj_lst: List of names for replication
    :return: List of references for the given object names
    """
    rep_lst = []
    for obj in obj_lst:
        rep_lst.append(find_obj_by_name(engine, database, obj).reference)
    return rep_lst


def get_running_job(engine, target_ref):
    """
    Function to find a running job from the DB target reference.
    :param engine: A Virtualization engine session object
    :param target_ref: Reference to the target of the running job
    :return:
    """
    return job.get_all(engine, target=target_ref,
                       job_state='RUNNING')[0].reference


def find_obj_list(obj_lst, obj_name):
    """
    Function to find an object in a list of objects
    obj_lst: List containing objects from the get_all() method
    obj_name: Name of the object to match
    :return: The named object. None is returned if no match is found.`
    """
    for obj in obj_lst:
        if obj_name == obj.name:
            return obj
    return None

def find_template_ref(engine, template_name):
    templates = template.get_all(engine)
    for t in templates:
        if t.name == template_name:
            return(t.reference)

    raise DlpxException('{} was not found.\n'.format(template_name))

def find_container_ref(engine, template_name, container_name):
    template_ref = find_template_ref(engine, template_name)
        
    containers = container.get_all(engine)
    for c in containers:
        if c.template != template_ref:
            continue

        if c.name == container_name:
            return(c.reference)

    raise DlpxException('{} was not found in template {}.\n'.format(container_name, template_name))

def find_branch_ref(engine, template_name, container_name, branch_name):
    container_ref = find_container_ref(engine, template_name, container_name)

    branches = branch.get_all(engine, container_ref)
    for b in branches:
        if b.name == branch_name:
            return b.reference

    raise DlpxException('{} was not found in container ref {}.\n'.format(branch_name, container_ref))

def find_bookmark_ref(engine, template_name, container_name, branch_name, bookmark_name):
    branch_ref = find_branch_ref(engine, template_name, container_name, branch_name)

    bookmarks = bookmark.get_all(engine)
    if container_name and branch_name:
        # container bookmark
        for bmark in bookmarks:
            if bmark.name == bookmark_name and bmark.branch == branch_ref and bmark.container_name == container_name and bmark.template_name == template_name:
                return bmark.reference
    else:
        # template bookmark
        for bmark in bookmarks:
            if bmark.name == bookmark_name and bmark.template_name == template_name:
                return bmark.reference
        
    raise DlpxException('{} was not found in container {}, branch {}.\n'.format(bookmark_name, container_name, branch_name))


def find_obj_by_name(engine, f_class, obj_name, active_branch=False):
    """
    Function to find objects by name and object class, and return object's
    reference as a string
    engine: A Delphix engine session object
    f_class: The objects class. I.E. database or timeflow.
    obj_name: The name of the object
    active_branch: Default = False. If true, return list containing
                   the object's reference and active_branch. Otherwise, return
                   the reference.
    """
    all_objs = f_class.get_all(engine)

    for obj in all_objs:
        if obj.name == obj_name:
            if active_branch is False:
                return(obj)

            #This code is for JS objects only.
            return_list = []
            return_list.append(obj.reference)
            return_list.append(obj.active_branch)
            return(return_list)

    #If the object isn't found, raise an exception.
    raise DlpxException('{} was not found.\n'.format(obj_name))

def find_source_by_dbname(engine, f_class, obj_name, active_branch=False):
    """
    Function to find sources by database name and object class, and return object's
    reference as a string
    engine: A Delphix engine session object
    f_class: The objects class. I.E. database or timeflow.
    obj_name: The name of the database object in Delphix
    active_branch: Default = False. If true, return list containing
                   the object's reference and active_branch. Otherwise, return
                   the reference.
    """

    try:
        all_objs = f_class.get_all(engine)
    except AttributeError as e:
        raise DlpxException('Could not find reference for object class'
                            '{}.\n'.format(e))
    for obj in all_objs:
        if obj.name == obj_name:
            source_obj = source.get_all(engine,database=obj.reference)
            return source_obj[0]

    #If the object isn't found, raise an exception.
    raise DlpxException('{} was not found on engine {}.\n'.format(
        obj_name, engine.address))


def get_obj_reference(engine, obj_type, obj_name, search_str=None,
                      container=False):
    """
    Return the reference for the provided object name
    engine: A Delphix engine object.
    results: List containing object name
    search_str (optional): string to search within results list
    container (optional): search for container instead of name
    """

    ret_lst = []

    results = obj_type.get_all(engine)

    for result in results:
        if container is False:
            if result.name == obj_name:
                ret_lst.append(result.reference)

                if search_str:
                    if re.search(search_str, result.reference, re.IGNORECASE):
                        ret_lst.append(True)
                    else:
                        ret_lst.append(False)

                return ret_lst
        else:
            if result.container == obj_name:
                ret_lst.append(result.reference)

                return ret_lst

    raise DlpxException('Reference not found for {}'.format(obj_name))


def find_obj_name(engine, f_class, obj_reference):
    """
    Return the obj name from obj_reference

    engine: A Delphix engine object.
    f_class: The objects class. I.E. database or timeflow.
    obj_reference: The object reference to retrieve the name
    """
    try:
        obj_name = f_class.get(engine, obj_reference)
        return obj_name.name

    except RequestError as e:
        raise DlpxException(e)

    except (JobError, HttpError) as e:
        raise DlpxException(e.message)


def find_dbrepo(engine, install_type, f_environment_ref, f_install_path):
    """
    Function to find database repository objects by environment reference and
    install path, and return the object's reference as a string
    You might use this function to find Oracle and PostGreSQL database repos.
    engine: Virtualization Engine Session object
    install_type: Type of install - Oracle, ASE, SQL
    f_environment_ref: Reference of the environment for the repository
    f_install_path: Path to the installation directory.
    return: delphixpy.web.vo.SourceRepository object
    """

    all_objs = repository.get_all(engine, environment=f_environment_ref)
    for obj in all_objs:
        if 'OracleInstall' == install_type:
            if (obj.type == install_type and
                obj.installation_home == f_install_path):

                return obj

        elif 'MSSqlInstance' == install_type:
            if (obj.type == install_type and
                obj.instance_name == f_install_path):

                return obj

        else:
            raise DlpxException('No Repo match found for type {}.\n'.format(
                install_type))

def find_sourceconfig(engine, sourceconfig_name, f_environment_ref):
    """
    Function to find database sourceconfig objects by environment reference and
    sourceconfig name (db name), and return the object's reference as a string
    You might use this function to find Oracle and PostGreSQL database
    sourceconfigs.
    engine: Virtualization Engine Session object
    sourceconfig_name: Name of source config, usually name of db
                       instnace (ie. orcl)
    f_environment_ref: Reference of the environment for the repository
    return: delphixpy.web.vo.SourceConfig object
    """

    all_objs = sourceconfig.get_all(engine, environment=f_environment_ref)
    for obj in all_objs:
        if obj.name == sourceconfig_name:
                return obj
        else:
            raise DlpxException('No sourceconfig match found for type {}.'
                                '\n'.format(sourceconfig_name))