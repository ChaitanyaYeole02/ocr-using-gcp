# Optical Character Recognition using GCP

<div align="justify">Optical Character Recognition (OCR for short) is a technique that converts digital images of text into machine-readable data. OCR is the process of converting scanned images of machine printed or handwritten text (numerals, letters, and
symbols), into machine readable character streams, plain (e.g. text files) or formatted (e.g. HTML files). OCR is a field of research in pattern recognition, artificial intelligence and computer vision. It is a common method of digitizing printed texts. <br>
OCR helps users by recognizing letters, numbers, and other written characters. What is even
more special about this is that it can convert images and scanned paper documents into
electronic data. These documents can be searchable through digital means, making for
seamless access.</div>

### Block Diagram
![ocr-using-gcp architecture](https://cloud.google.com/static/functions/img/gcf-ocr.svg) <br>

### Methodology
1. [Set up the Google Vision API.](https://cloud.google.com/vision/docs/setup)
2. After creating the JSON key file, set the environment variable as ```GOOGLE_APPLICATION_CREDENTIALS='/path_to_the_file/key.json'```
3. Run ```main.py``` using Python3.9