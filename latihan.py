import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QGridLayout, QTableWidget,
    QTableWidgetItem
)
from PyQt5.QtCore import Qt

class MahasiswaApp(QWidget):
    def __init__(self):  # Perbaikan dari _init_
        super().__init__()  # Perbaikan dari _init_
        self.setWindowTitle("MAHASISWA")
        self.setGeometry(100, 100, 800, 400)
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()

        # Label Judul
        title_label = QLabel("MAHASISWA")
        title_label.setStyleSheet("font-size: 18pt; font-weight: bold; background-color: lightcyan;")
        title_label.setFixedHeight(40)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Form
        grid = QGridLayout()
        labels = ["NPM", "NAMA LENGKAP", "NAMA PANGGILAN", "TELEPON", "EMAIL", "KELAS", "MATAKULIAH", "LOKASI KAMPUS"]
        self.inputs = {}

        for i, label in enumerate(labels):
            lbl = QLabel(label)
            line_edit = QLineEdit()
            self.inputs[label] = line_edit
            grid.addWidget(lbl, i, 0)
            grid.addWidget(line_edit, i, 1)

        layout.addLayout(grid)

        # Tombol Aksi
        button_layout = QHBoxLayout()
        btn_tambah = QPushButton("TAMBAH")
        btn_ubah = QPushButton("UBAH")
        btn_hapus = QPushButton("HAPUS")
        btn_batal = QPushButton("BATAL")

        btn_tambah.clicked.connect(self.tambah_data)

        for btn in (btn_tambah, btn_ubah, btn_hapus, btn_batal):
            button_layout.addWidget(btn)

        layout.addLayout(button_layout)

        # Tabel
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "NPM", "NAMA LENGKAP", "NAMA PANGGILAN", "TELEPON",
            "EMAIL", "KELAS", "MATAKULIAH", "LOKASI KAMPUS"
        ])
        layout.addWidget(self.table)

        self.setLayout(layout)

    def tambah_data(self):
        row = self.table.rowCount()
        self.table.insertRow(row)
        for i, key in enumerate([
            "NPM", "NAMA LENGKAP", "NAMA PANGGILAN", "TELEPON",
            "EMAIL", "KELAS", "MATAKULIAH", "LOKASI KAMPUS"
        ]):
            self.table.setItem(row, i, QTableWidgetItem(self.inputs[key].text()))

if __name__ == "__main__":  # Perbaikan dari _name_
    app = QApplication(sys.argv)
    window = MahasiswaApp()
    window.show()
    sys.exit(app.exec_())
