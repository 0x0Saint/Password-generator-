from PyQt5.QtWidgets import QApplication
from password_generator import generate_password
from ui import PasswordGeneratorApp
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.generate_password = generate_password  # Assign the password generation function to the window's attribute
    window.show()
    sys.exit(app.exec_())
