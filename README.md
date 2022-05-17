# pyqt-transparent-button-background-animation-example
PyQt example of transparent button's background animation

This example shows the transparent background button (button's text is visible) reveal the color with animation when you put the mouse cursor in it.

This can't be done by QGraphicsOpacityEffect which is normally used at opacity transition.

Because if you use QGraphicsOpacityEffect, everything become invisible at the transparent state. 

So i use stylesheet instead.

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install git+https://github.com/yjg30737/pyqt-transparent-button-background-animation-example.git --upgrade`

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_transparent_button_background_animation_example import MainWindow

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
```

Result

https://user-images.githubusercontent.com/55078043/168700640-05a64ab3-d09d-4bca-8e53-20677feba60f.mp4

