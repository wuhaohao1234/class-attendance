import { defineConfig } from 'vite';
import postcss from 'rollup-plugin-postcss';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [
    // postcss({
    //   config: './tailwind.config.js',
    //   inject: true,
    // }),
    vue()
  ],
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    }
  }
});
