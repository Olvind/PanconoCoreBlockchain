import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

# ---- Tokenomics ----
TOTAL_SUPPLY = 15_000_000
TREASURER_BALANCE = 2_000_000
RESERVED_BALANCE = 650_000   # 54,167 wallets × 12 PANNO
RESERVED_BALANCE_A = 5_000_000   # 10,000 wallets × 500 PANNO
RESERVED_BALANCE_B = 2_000_000   # 1,000 wallets × 2000 PANNO
MINEABLE_BALANCE = TOTAL_SUPPLY - (TREASURER_BALANCE + RESERVED_BALANCE)

class PanconoWallet(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pancono Wallet")
        self.setGeometry(300, 200, 400, 250)

        layout = QVBoxLayout()

        title = QLabel("<h2>Pancono Core Wallet</h2>")
        layout.addWidget(title)

        layout.addWidget(QLabel(f"💰 Total Supply: {TOTAL_SUPPLY:,} PANNO"))
        layout.addWidget(QLabel(f"🏦 Treasurer Wallet: {TREASURER_BALANCE:,} PANNO"))
        layout.addWidget(QLabel(f"📦 Reserved Wallets: {RESERVED_BALANCE:,} PANNO"))
        layout.addWidget(QLabel(f"📦 Reserved Wallets A: {RESERVED_BALANCE:,} PANNO"))
        layout.addWidget(QLabel(f"📦 Reserved Wallets:B {RESERVED_BALANCE:,} PANNO"))
        layout.addWidget(QLabel(f"⚡ Remaining Mineable: {MINEABLE_BALANCE:,} PANNO"))

        refresh_btn = QPushButton("🔄 Refresh Balances")
        layout.addWidget(refresh_btn)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wallet = PanconoWallet()
    wallet.show()
    sys.exit(app.exec_())
