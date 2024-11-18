import qrcode

# Ask the user to input the website link
website_link = input("Enter the website link to generate a QR code: ")

# Create and configure the QR code
qr = qrcode.QRCode(version=1, box_size=5, border=5)
qr.add_data(website_link)
qr.make()

# Generate the QR code image
img = qr.make_image(fill_color='black', back_color='white')

# Save the QR code image
file_name = "generated_qr.png"
img.save(file_name)

print(f"QR code successfully generated and saved as '{file_name}'.")