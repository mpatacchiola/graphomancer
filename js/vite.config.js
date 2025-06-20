import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    lib: {
      entry: 'src/index.js',
      name: 'GraphomancerJS',
      fileName: (format) => `graphomancer-js.${format}.js`
    },
    rollupOptions: {
      external: ['echarts'],
      output: {
        globals: {
          echarts: 'echarts'
        }
      }
    }
  }
})
