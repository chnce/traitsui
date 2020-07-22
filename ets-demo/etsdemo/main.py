# (C) Copyright 2020 Enthought, Inc., Austin, TX
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in LICENSE.txt and may be redistributed only under
# the conditions described in the aforementioned license. The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
#
# Thanks for using Enthought open source!

""" The main function for launching the demo application.
"""

from etsdemo.app import Demo, DemoVirtualDirectory
from etsdemo.loader import get_responses, response_to_node


#: Default application title
_TITLE = "Enthought Tool Suite"


def _create_demo(infos=None, title=_TITLE):
    """ Create the demo object with everything setup ready to be launched.

    Parameters
    ----------
    infos : list of dict, or None
        List of responses specifying the demo resources.
        Each response is a dictionary, in the format as specified by an
        entry point.
        If none, then responses are loaded from existing entry points installed
        in the Python environment.
    title : str, optional
        Default application title.

    Returns
    -------
    demo : Demo
    """
    if infos is None:
        infos = get_responses()

    resources = [
        response_to_node(response)
        for response in infos
    ]
    return Demo(
        title=title,
        model=DemoVirtualDirectory(resources=resources),
    )


def main(infos=None, title=_TITLE):
    """ Main function for launching the demo application.

    Parameters
    ----------
    infos : list of dict, or None
        List of responses specifying the demo resources.
        Each response is a dictionary, in the format as specified by an
        entry point. This allows packages to launch the demo application
        with their own set of data files without the entry points and without
        having to load files from other packages.
        If none, then responses are loaded from existing entry points installed
        in the Python environment.
    title : str, optional
        Default application title.
    """
    demo = _create_demo(infos=infos, title=title)
    demo.configure_traits()