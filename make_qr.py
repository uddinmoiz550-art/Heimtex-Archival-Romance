"""Make a print-ready vector QR PDF.  Usage:  python make_qr.py https://YOURNAME.github.io/heimtex/
Setup once:  pip install qrcode reportlab"""
import sys, qrcode
from qrcode.constants import ERROR_CORRECT_Q
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
url = sys.argv[1]
q = qrcode.QRCode(error_correction=ERROR_CORRECT_Q, border=0); q.add_data(url); q.make(fit=True)
m = q.get_matrix(); n = len(m)
page, size = 70*mm, 50*mm; mod = size/n; o = (page-size)/2
c = canvas.Canvas("heimtex-qr.pdf", pagesize=(page, page)); c.setFillColorRGB(0,0,0)
for y,row in enumerate(m):
    for x,v in enumerate(row):
        if v: c.rect(o+x*mod, page-o-(y+1)*mod, mod+.01, mod+.01, stroke=0, fill=1)
c.save(); print("Wrote heimtex-qr.pdf for", url)
