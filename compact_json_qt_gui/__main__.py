import json
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
        self.text_edit = QPlainTextEdit('{"Hello": ["This", "is"], "some": "sample", "input": ["which", "you", "can", "format", "by", "clicking"]}')
        self.button = QPushButton("Format")
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.format_text)

        self._formatter = compact_json.Formatter(ensure_ascii=False, max_inline_complexity=2, indent_spaces=2)

    def format_text(self) -> None:
        self.button.setEnabled(False)
        text = self.text_edit.toPlainText()
        formatted = self._formatter.serialize(json.loads(json.dumps(json.loads(text), sort_keys=True)))
        self.text_edit.setPlainText(formatted)
        self.button.setEnabled(True)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    retval = app.exec()
    sys.exit(retval)


if __name__ == "__main__":
    main()
