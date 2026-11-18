# Heimtextil – Archival Romance (open product page)
Open-source product page opened by scanning the QR code on the Heimtex bedding set. Works in any phone browser; no app or account needed.

## Files
- `index.html` – the whole site. Product data is the `PRODUCTS` block at the top of the script.
- `images/` – hero photo, logo, one fabric swatch per layer.
- `make_qr.py` – turns your final web address into a print-ready QR PDF.
- `LICENSE` – MIT.

## Publish (free, ~5 minutes)
1. Create an account at github.com (use a company email) and a **public** repository named `heimtex`.
2. Upload every file in this folder (Add file → Upload files).
3. Settings → Pages → Branch `main`, folder `/ (root)` → Save.
4. Your permanent link is `https://<account>.github.io/heimtex/`. For a branded link, add a custom domain in the same Pages screen.
5. Run `python make_qr.py <that link>` and send `heimtex-qr.pdf` to print.

## Add more products later
Copy the product object in `PRODUCTS`, change the `slug`, text and images. Link it as `.../heimtex/#new-slug`. The same QR keeps working; you only change content behind it.

## 3D / AR
The 3D layer view is built in. True AR ("place on my bed") needs a 3D model (.glb) of the bed set from a 3D artist or photogrammetry; once you have it, set `model:"images/bed.glb"` and ask to wire up `<model-viewer>`.

## Scan analytics
Uncomment the GoatCounter line at the bottom of `index.html` (free, cookie-less).
