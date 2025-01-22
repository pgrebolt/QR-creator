# Basic QR code creator using Segno library

import segno

url = "https://onlinelibrary.wiley.com/doi/full/10.1002/smsc.202400066"
red_color = '#d11d33'

qrcode = segno.make_qr(url)

qrcode.save("qr_article.png",
            scale = 5,
            border = 2,
            dark = '#4472C4',
            light = 'white',
            dpi=600)