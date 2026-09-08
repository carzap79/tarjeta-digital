# -*- coding: utf-8 -*-
"""Adapta la salida estática (dist/) para servirla bajo una ruta base, p. ej. /tarjeta-digital/sitio.

Uso: python3 herramientas/ruta_base.py dist /tarjeta-digital/sitio
- Reescribe los enlaces y rutas absolutas (href, src, poster, action, srcset, url()) para que cuelguen de la ruta base.
- Marca las páginas como vista previa (noindex) y retira robots.txt, sitemap.xml y _headers, que solo aplican al sitio real.
"""
import os
import re
import sys

dist, base = sys.argv[1], sys.argv[2].rstrip('/')

for nombre in ('robots.txt', 'sitemap.xml', '_headers'):
    ruta = os.path.join(dist, nombre)
    if os.path.exists(ruta):
        os.remove(ruta)

patron_attr = re.compile(r'(\s(?:href|src|poster|action|srcset))="/(?!/)')
patron_url = re.compile(r'url\((["\']?)/(?!/)')
for carpeta, _, archivos in os.walk(dist):
    for archivo in archivos:
        if not archivo.endswith(('.html', '.css', '.js')):
            continue
        ruta = os.path.join(carpeta, archivo)
        with open(ruta, encoding='utf8') as f:
            contenido = f.read()
        nuevo = patron_attr.sub(lambda m: f'{m.group(1)}="{base}/', contenido)
        nuevo = patron_url.sub(lambda m: f'url({m.group(1)}{base}/', nuevo)
        if archivo.endswith('.html') and '<meta name="robots"' not in nuevo:
            nuevo = nuevo.replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="robots" content="noindex, nofollow">', 1)
        if nuevo != contenido:
            with open(ruta, 'w', encoding='utf8') as f:
                f.write(nuevo)
print('ruta base aplicada:', base)
