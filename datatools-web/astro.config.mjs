import { defineConfig } from 'astro/config';

// Sitio estático. Cambia `site` cuando el dominio definitivo esté apuntado.
export default defineConfig({
  site: 'https://www.datatools.com.co',
  output: 'static',
  trailingSlash: 'never',
  // `assets: 'recursos'` evita la carpeta `_astro`, que GitHub Pages (Jekyll) ignoraría en la vista previa.
  build: { format: 'directory', assets: 'recursos' },
});
