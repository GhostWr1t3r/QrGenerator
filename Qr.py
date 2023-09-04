# importing the qrcode library  
import qrcode  
# generating a QR code using the make() function  
qr_img = qrcode.make(input("Enter anything: "))  
# saving the image file  
qr_img.save("QR.jpg")  
