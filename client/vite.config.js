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
});
