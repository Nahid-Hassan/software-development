from qrcode import make
from cv2 import imread, QRCodeDetector

def generate_qrcode(data):
    img = make(data)
    return img


def save_img(img):
    img.save('qrdata.jpg')

def decode_qrcode(source):
    decoder = QRCodeDetector()
    val, *rest = decoder.detectAndDecode(imread(source))
    return val

def main():
    img = generate_qrcode(input("Enter any text: "))
    save_img(img)
    print("QR code image is saved")
    val = decode_qrcode('qrdata.jpg')
    print(val)


if __name__ == "__main__":
    main()
