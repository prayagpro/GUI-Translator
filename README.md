# 🌐 GUI Translator

**GUI Translator** is a Python-based language translation tool that provides a simple and clean graphical user interface using **Tkinter**. It supports translations between 30+ languages, making it a powerful tool for quick and efficient translations.

---

## 🚀 Features

- **User-Friendly GUI:** Built with Tkinter for a clean and intuitive interface.
- **Multi-Language Support:** Translate text between more than 30 languages.
- **Real-Time Translation:** Instant results for entered text.
- **Error Handling:** Displays appropriate error messages for failed translations.

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/GUI-Translator.git
cd GUI-Translator
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
python3 -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### Note:
Ensure **Python 3.10+** is installed with Tcl/Tk support. If Tkinter is not working, refer to the [Troubleshooting](#❓-troubleshooting) section below.

---

## 🎉 Usage

1. Run the `google_trans.py` script:
   ```bash
   python google_trans.py
   ```
2. Enter the text in the **Source Text** box.
3. Select the **Source Language** and **Target Language** from the dropdown menus.
4. Click the **Translate** button to see the translated text in the **Destination Text** box.

---

## 🌏 Supported Languages

The application supports a wide range of languages, including:

- **English**
- **Spanish**
- **French**
- **German**
- **Hindi**
- **Chinese**
- **Japanese**
- **Russian**
- **Arabic**
- **Portuguese**
- ...and many more!

---

## ❓ Troubleshooting

### Issue: Tkinter Not Found
If you encounter:
```plaintext
ModuleNotFoundError: No module named '_tkinter'
```
Follow these steps:

1. Install Tcl/Tk using Homebrew:
   ```bash
   brew install tcl-tk
   ```
2. Add Tcl/Tk paths to your environment:
   ```bash
   export PATH="/opt/homebrew/opt/tcl-tk/bin:$PATH"
   export LDFLAGS="-L/opt/homebrew/opt/tcl-tk/lib"
   export CPPFLAGS="-I/opt/homebrew/opt/tcl-tk/include"
   export PKG_CONFIG_PATH="/opt/homebrew/opt/tcl-tk/lib/pkgconfig"
   ```
3. Reinstall Python with Tcl/Tk support:
   ```bash
   brew reinstall python@3.10
   ```

---

## 🤝 Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message"
   ```
4. Push and open a Pull Request.

---
## 🙏 Acknowledgments

- **Tkinter:** For GUI design.
- **translate library:** For language translations.
- Inspired by translation tools like **Google Translate**.

---
