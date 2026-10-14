"""Regenerate the QR code for the live site.

    pip install segno
    python3 qr.py                 # uses LIVE_URL below
    python3 qr.py https://...     # any other URL

Writes assets/qr.svg (shown bottom-left on the page) and assets/qr.png
(1184 px, for the poster / slides).
"""
import sys
import segno

LIVE_URL = 'https://sriman22-ui.github.io/cc6/'

url = sys.argv[1] if len(sys.argv) > 1 else LIVE_URL
qr = segno.make(url, error='m')
qr.save('assets/qr.svg', scale=8, border=2, dark='#173a5e', light='#ffffff')
qr.save('assets/qr.png', scale=32, border=4, dark='#173a5e', light='#ffffff')
print(f'{url} -> assets/qr.svg, assets/qr.png ({qr.designator})')
