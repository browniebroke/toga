from java import jclass

from android.os import Build

from .base import SimpleProbe
from .properties import toga_alignment, toga_color, toga_font


class LabelProbe(SimpleProbe):
    native_class = jclass("android.widget.TextView")

    @property
    def color(self):
        return toga_color(self.native.getCurrentTextColor())

    @property
    def text(self):
        return str(self.native.getText())

    @property
    def font(self):
        return toga_font(
            self.native.getTypeface(),
            self.native.getTextSize(),
            self.native.getResources(),
        )

    @property
    def alignment(self):
        justification_mode = (
            None if Build.VERSION.SDK_INT < 26 else self.native.getJustificationMode()
        )
        return toga_alignment(self.native.getGravity(), justification_mode)
