# Sitio web de Data Tools S.A.S

Sitio estático construido con [Astro](https://astro.build) y desplegado en Cloudflare Pages.
Todo el contenido está en español; los textos viven en archivos de datos para poder editarlos sin tocar el diseño.

## Estructura

```
src/
  data/            ← contenido editable (JSON)
    sitio.json       datos de contacto, navegación, enlaces legales
    soluciones.json  las seis líneas de servicio (textos, listas, fichas técnicas)
    productos.json   Circulemos y CiDi
    casos.json       clientes, cifras, líneas de trabajo, sectores, clientes de salud, trayectoria
    faq.json         preguntas frecuentes del inicio
  pages/           ← una página por archivo (inicio, soluciones, productos, casos, dato-ia, nosotros, contacto, gracias, legales, 404)
  components/      ← cabecera, pie, logo, sección, tarjeta de cierre, preguntas, ficha técnica
  layouts/         ← plantilla base (metadatos, fuentes, datos estructurados)
  styles/          ← global.css: paleta, tipografía y componentes
public/
  media/           ← imágenes de Dato (WebP), video y póster
  logo-datatools.svg, logo-datatools-sello.svg, favicon.svg, apple-touch-icon.png
  robots.txt, sitemap.xml, _headers (cabeceras de seguridad y caché)
functions/
  api/contacto.js  ← función de Cloudflare Pages que envía el formulario por correo (Resend)
```

## Trabajar en local

```bash
npm install
npm run dev        # http://localhost:4321
npm run build      # genera dist/
```

Requiere Node 20 o superior (el archivo `.node-version` fija la 22 para Cloudflare).

## Desplegar en Cloudflare Pages (una sola vez)

1. Sube este repositorio a GitHub.
2. En el panel de Cloudflare: **Workers & Pages → Create → Pages → Connect to Git** y elige el repositorio.
3. Configuración de compilación: *Framework preset* **Astro**, *Build command* `npm run build`, *Build output directory* `dist`.
4. Guarda. Cada rama genera una URL de vista previa; la rama `main` es producción.
5. Cuando esté listo, en **Custom domains** agrega `www.datatools.com.co` (y redirige el dominio raíz).

## Activar el formulario de contacto

El formulario envía los mensajes por correo a través de [Resend](https://resend.com) (plan gratuito suficiente para un sitio corporativo).

1. Crea una cuenta en Resend, verifica el dominio `datatools.com.co` y genera una clave de API.
2. En Cloudflare Pages: **Settings → Environment variables** (producción y vista previa):
   - `RESEND_API_KEY` = la clave de API
   - `CONTACTO_DESTINO` = correo(s) que reciben los mensajes, separados por coma
   - `CONTACTO_REMITENTE` = remitente verificado, p. ej. `web@datatools.com.co`
3. Vuelve a desplegar. Sin estas variables el sitio funciona igual y el formulario muestra el aviso para llamar al PBX.

## Cómo editar el contenido

- **Textos de soluciones, productos, casos y preguntas**: edita el JSON correspondiente en `src/data/`. No hace falta tocar las páginas.
- **Dirección, teléfono, correo, horario, redes**: `src/data/sitio.json`. El correo aparece en el pie y en Contacto solo cuando el campo `correo` tiene valor.
- **Enlaces a la intranet y autoservicios**: `enlacesInternos` en `sitio.json`; se muestran solo si tienen URL.
- **Textos de la página de inicio, Dato IA y Nosotros**: están en sus archivos `.astro` (parte superior, en variables) porque son propios de cada página.
- **Logo**: `public/logo-datatools.svg` (marca sobre transparente, cabecera) y `public/logo-datatools-sello.svg` (disco blanco, pie). Para usar una versión en vector, reemplaza los archivos o cambia las rutas en `src/components/Logo.astro`.
- **Imágenes de Dato**: `public/media/`. Las versiones `-recorte.webp` tienen fondo transparente para usarlas sobre fondos oscuros.
- **Dominio**: cambia `site` en `astro.config.mjs` y las URL de `public/sitemap.xml` y `public/robots.txt` si el dominio definitivo es distinto.

## Pendientes antes de publicar

- [x] Logo oficial: se tomó de www.datatools.com.co (`public/logo-datatools.svg`, `public/logo-datatools-sello.svg`, `public/favicon.svg`; son SVG que envuelven el PNG oficial de 246×173). Si existe la versión en vector (SVG/AI/PDF), reemplazar esos archivos mejora la nitidez en pantallas grandes.
- [x] Valores corporativos, misión, visión, alcance y política del SIG y Código de Ética: tomados del sitio oficial (los textos legales enlazan a los PDF oficiales GJ-PT-01, GJ-FM-01 y GJ-FM-02).
- [ ] Correo de destino del formulario y variables de Resend.
- [ ] Textos base de política de privacidad, términos y habeas data: confirmar con el área jurídica (los documentos oficiales ya están enlazados).
- [ ] Año de fundación: el sitio oficial muestra 1997 en la imagen actual de «Quiénes somos» y 1987 en una versión anterior; el sitio nuevo usa 1997. Confirmar.
- [ ] Confirmar cifras: +5 millones de transacciones al año y 99,9 % de disponibilidad (tomadas de web-datatools.pages.dev); 85 profesionales y listado de las 900 empresas de Semana (sitio oficial).
- [ ] Confirmar la descripción de CiDi (Centro Integral de Información: infractores, contravencional, cartera y cobro, trámites en línea) y los clientes que se pueden mostrar con nombre.
- [ ] Confirmar la redacción sobre ISO/IEC 42001 (hoy: «sistema de gestión con la norma como referencia», sin afirmar certificación).
- [ ] Logos de clientes autorizados, si se quieren mostrar en el inicio.
