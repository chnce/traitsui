"""
This demo shows you how to use animated GIF files in a traits user interface.
"""

from os.path \
    import join, dirname
    
from enthought.traits.api \
    import HasTraits, File, Bool, Int
    
from enthought.traits.ui.api \
    import View, VGroup, HGroup, Item, EnumEditor
    
from enthought.traits.ui.wx.animated_gif_editor \
    import AnimatedGIFEditor

# Some sample animated GIF files:    
import enthought.traits.ui as ui

base_path = join( dirname( ui.api.__file__ ), 'demo', 'Extras', 'images' )

files = [
    join( base_path, 'logo_64x64.gif' ),
    join( base_path, 'logo_48x48.gif' ),
    join( base_path, 'logo_32x32.gif' )
]

class AnimatedGIFDemo ( HasTraits ):
    
    # The animated GIF file to display:
    gif_file = File( files[0] )
                 
    # Is the animation playing or not?
    playing = Bool( True )
                 
    # The traits view:
    view = View(
        VGroup(
            HGroup(
                Item( 'gif_file', 
                      editor     = AnimatedGIFEditor( playing = 'playing' ),
                      show_label = False ),
                Item( 'playing' ),
            ),
            '_',
            Item( 'gif_file', 
                  label  = 'GIF File',
                  editor = EnumEditor( values = files )
            )
        ),
        title   = 'Animated GIF Demo',
        buttons = [ 'OK' ]
    )
                         
demo = AnimatedGIFDemo()

if __name__ == '__main__':
    demo.configure_traits()
