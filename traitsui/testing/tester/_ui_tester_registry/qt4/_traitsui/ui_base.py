#  Copyright (c) 2005-2020, Enthought, Inc.
#  All rights reserved.
#
#  This software is provided without warranty under the terms of the BSD
#  license included in LICENSE.txt and may be redistributed only
#  under the conditions described in the aforementioned license.  The license
#  is also available online at http://www.enthought.com/licenses/BSD.txt
#
#  Thanks for using Enthought open source!
#
from traitsui.qt4.ui_base import ButtonEditor
from traitsui.testing.api import DisplayedText, IsEnabled, MouseClick
from traitsui.testing.tester._ui_tester_registry.qt4 import (
    _interaction_helpers
)


def register(registry):
    """ Register solvers/handlers specific to qt ui_base Editors
    for the given registry.

    If there are any conflicts, an error will occur.

    Parameters
    ----------
    registry : TargetRegistry
    """
    handlers = [
        (MouseClick,
            (lambda wrapper, _: _interaction_helpers.mouse_click_qwidget(
                wrapper._target.control, wrapper.delay))),
        (DisplayedText,
            lambda wrapper, _: wrapper._target.control.text()),
        (IsEnabled, lambda wrapper, _: wrapper._target.control.isEnabled()),
    ]
    for interaction_class, handler in handlers:
        registry.register_interaction(
            target_class=ButtonEditor,
            interaction_class=interaction_class,
            handler=handler
        )