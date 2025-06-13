# Text-Extraction-OCR-Tesseract


# 📝 PDF OCR Text Extractor 

This Python tool extracts text from PDF files using **OCR (Optical Character Recognition)** with **Tesseract** and **Poppler**.

---

## 🚀 Features

- Convert PDF pages to images with Poppler
- Extract French or English text from images using Tesseract OCR
- Output the recognized text to a `.txt` file
- Command-line interface for easy use

---

## 🔧 Setup Instructions

### 1. Install and Configure Poppler on Windows

#### 📥 Step 1: Download Poppler

Download the latest release from:  
👉 [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/)

Extract the ZIP to a known location, e.g.: C:\poppler


#### ⚙️ Step 2: Add Poppler to your System PATH

1. Open **Start Menu** → Search for **Environment Variables**  
2. Click **"Edit the system environment variables"**  
3. In the **System Properties** window, click **Environment Variables...**  
4. Under **System variables**, find and select `Path`, then click **Edit**  
5. Click **New** and add: C:\poppler\Library\bin

6. Click **OK** to close all windows

#### ✅ Step 3: Verify Installation

Open **Command Prompt** and run:

```bash
pdfinfo
```
You should see Poppler's help output, confirming it's properly installed.


### 2. Install Tesseract OCR
#### 📥 Step 1: Download Tesseract
Get the Windows installer from:
👉 [Tesseract Installation](https://docs.coro.net/featured/agent/install-tesseract-windows/)

Install to a folder such as:

C:\Program Files\Tesseract-OCR

#### ⚙️ Step 2: Add Tesseract to your System PATH

1. Open **Start Menu** → Search for **Environment Variables**  
2. Click **"Edit the system environment variables"**  
3. In the **System Properties** window, click **Environment Variables...**  
4. Under **System variables**, find and select `Path`, then click **Edit**  
5. Click **New** and add: C:\Program Files\Tesseract-OCR

6. Click **OK** to close all windows

#### 🌍 Step 3: Download Language Packs (e.g., French)
Install during Tesseract setup

Or manually download from: [tessdata](https://github.com/tesseract-ocr/tessdata/blob/main/fra.traineddata)
and place the .traineddata file (e.g., fra.traineddata) to your system PATH variable (follow same steps as for Poppler):


#### ✅ Step 4: Verify Installation
Run this in Command Prompt:

```bash
tesseract --version
```

#### ✅ Step 5: Libraries installation

Clone the GitHub repo using:

```bash
git clone https://github.com/nguefackuriel/Text-Extraction-OCR-Tesseract.git
```

Run this in Command Prompt:

```bash
cd ocr_tesseract
```

Run this in Command Prompt:

```bash
pip install -r requirements.txt
```

#### ✅ Step 6: Run the code
Run this in Command Prompt:

```bash
python ocr_tesseract.py pdf_file.pdf output_file.txt
```

for example:

```bash
python ocr_tesseract.py D:\Downloads_Uriel\ordo_1.pdf D:\Downloads_Uriel\ordo_1.txt
```
