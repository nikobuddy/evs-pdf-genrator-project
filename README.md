
# 🌱 EVS Project PDF Generator

This Python script generates well-formatted **EVS project PDFs** using [Wikipedia](https://wikipedia.org) content and the ReportLab library. Each topic is automatically researched, structured into sections like **Acknowledgement**, **Introduction**, **Case Studies**, and **Conclusion**, and then exported as a polished A4-sized PDF.

Perfect for students or educators looking to create environment-related project files quickly and efficiently.

---

## 📁 Features

- 🔍 Fetches topic content automatically from Wikipedia
- 📄 Structured sections in each PDF:
  - Acknowledgement
  - Introduction
  - Types
  - Case Studies
  - Conclusion
- 🌊 Includes a watermark image if available
- 📂 Outputs neatly into a separate folder (`evs_pdfs`)
- 🧠 Uses clean formatting with ReportLab styles

---

## 🔧 Requirements

Install the necessary Python packages using pip:

```bash
pip install wikipedia reportlab
```

---

## 🚀 Usage

1. Place your watermark image as `watermaeks.png` in the same directory.
2. Run the script:

```bash
python evs_pdf_generator.py
```

3. All the PDFs will be saved in the `evs_pdfs` folder.

> You can customize the topic list in the `evs_topics` variable inside the script.

---

## 📥 Download

Click the button below to download the script:

[![Download Script](https://img.shields.io/badge/Download-Python%20Script-blue?style=for-the-badge&logo=python)](https://your-download-link.com/evs_pdf_generator.py)

> Replace the above link (`https://your-download-link.com/evs_pdf_generator.py`) with the actual location of your script (e.g., Google Drive, GitHub raw link).

---

## 📝 Notes

- This script uses Wikipedia summaries, so internet access is required.
- Not all topics may return valid content due to missing Wikipedia pages.
- Content is limited to ~3000 words per topic to keep PDF sizes manageable.

---

## 📌 Author

Made with ❤️ by **Ram Lokhande**  
📚 EVS Project's PDF'S - *"Download app from Play Store"*

---

## 📃 License

This project is licensed under the MIT License.
