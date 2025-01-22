# Basic QR code creator using Segno library

# Import Segno library
import segno

# Define file or URL to encode
url = "https://onlinelibrary.wiley.com/doi/full/10.1002/smsc.202400066"

# Define saving name
saving_name = "qr_article.png"

red_color = '#d11d33' # (color vermell correbars)

# Create the QR code
qrcode = segno.make_qr(url)

# Save the QR code with the desired properties
qrcode.save(saving_name,
            scale = 5,
            border = 2,
            dark = '#4472C4',
            light = 'white',
            dpi=600)
