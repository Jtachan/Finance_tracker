"""Here is contained the script to launch the app."""

import sys

from PyQt6.QtWidgets import QApplication

from split_mate.gui import SplitMateWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplitMateWindow()
    window.show()
    sys.exit(app.exec())
