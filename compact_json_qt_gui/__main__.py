import json
import tempfile
import subprocess
import sys

import compact_json

from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget
from PySide6.QtWidgets import QPlainTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle("JSON Formatter")

        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        layout = QVBoxLayout()
        self.widget.setLayout(layout)
        self.text_edit = QPlainTextEdit("def format_me(): print('Please!')")
        self.button = QPushButton("Format")
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.format_text)

    def format_text(self) -> None:
        text = self.text_edit.toPlainText()
        text = json.dumps(json.loads(text), sort_keys=True)
        self.button.setEnabled(False)

        compact_json.
        with tempfile.NamedTemporaryFile("w+") as f:
            f.write(text)
            f.seek(0)
            output = subprocess.run(
                [
                    "compact-json",
                    "--max-compact-list-complexity",
                    "2",
                    "-l",
                    "80",
                    "--indent",
                    "2",
                    "--no-ensure-ascii",
                    f.name,
                ],
                capture_output=True,
            )
            print(output)
        if output.returncode == 0:
            self.text_edit.setPlainText(output.stdout.decode())
        self.button.setEnabled(True)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    retval = app.exec()
    sys.exit(retval)


if __name__ == "__main__":
    main()
