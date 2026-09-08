import { defineConfig } from 'astro/config';

// Sitio estático. Cambia `site` cuando el dominio definitivo esté apuntado.
export default defineConfig({
  site: 'https://www.datatools.com.co',
  output: 'static',
  trailingSlash: 'never',
  build: { format: 'directory' },
});
