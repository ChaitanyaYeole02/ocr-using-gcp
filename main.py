import io
import cv2
from PIL import Image

# Imports the Google Cloud client library
from google.cloud import translate_v2 as translate
from google.cloud import vision
from google.cloud.vision_v1 import types


def translation_test(text):
    target = 'zh-CN'    # zh-CN Mandarin
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target)
    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))


# Instantiates a client
client = vision.ImageAnnotatorClient()


def detect_text(path):
    """Detects text in the file."""
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    string = ''

    for text in texts:
        string+=' ' + text.description
    return string


cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    file = 'live.png'
    cv2.imwrite(file, frame)

    # print OCR text
    ocr_text = detect_text(file)
    print(ocr_text)
    translation_test(ocr_text)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
