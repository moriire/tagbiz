// vite.config.js
import { fileURLToPath, URL } from "node:url";
import { defineConfig } from "file:///home/baun/web/tagbiz/biz/node_modules/vite/dist/node/index.js";
import vue from "file:///home/baun/web/tagbiz/biz/node_modules/@vitejs/plugin-vue/dist/index.mjs";
import vueJsx from "file:///home/baun/web/tagbiz/biz/node_modules/@vitejs/plugin-vue-jsx/dist/index.mjs";
import { resolve } from "path";
var __vite_injected_original_dirname = "/home/baun/web/tagbiz/biz";
var __vite_injected_original_import_meta_url = "file:///home/baun/web/tagbiz/biz/vite.config.js";
var vite_config_default = defineConfig({
  base: "/tagbiz/",
  plugins: [
    vue(),
    vueJsx()
  ],
  build: {
    outDir: "dist",
    // Output directory
    rollupOptions: {
      input: resolve(__vite_injected_original_dirname, "index.html")
      // Entry point for the build
    }
  },
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", __vite_injected_original_import_meta_url))
    }
  }
});
export {
  vite_config_default as default
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsidml0ZS5jb25maWcuanMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbImNvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9kaXJuYW1lID0gXCIvaG9tZS9iYXVuL3dlYi90YWdiaXovYml6XCI7Y29uc3QgX192aXRlX2luamVjdGVkX29yaWdpbmFsX2ZpbGVuYW1lID0gXCIvaG9tZS9iYXVuL3dlYi90YWdiaXovYml6L3ZpdGUuY29uZmlnLmpzXCI7Y29uc3QgX192aXRlX2luamVjdGVkX29yaWdpbmFsX2ltcG9ydF9tZXRhX3VybCA9IFwiZmlsZTovLy9ob21lL2JhdW4vd2ViL3RhZ2Jpei9iaXovdml0ZS5jb25maWcuanNcIjtpbXBvcnQgeyBmaWxlVVJMVG9QYXRoLCBVUkwgfSBmcm9tICdub2RlOnVybCdcblxuaW1wb3J0IHsgZGVmaW5lQ29uZmlnIH0gZnJvbSAndml0ZSdcbmltcG9ydCB2dWUgZnJvbSAnQHZpdGVqcy9wbHVnaW4tdnVlJ1xuaW1wb3J0IHZ1ZUpzeCBmcm9tICdAdml0ZWpzL3BsdWdpbi12dWUtanN4J1xuaW1wb3J0IHsgcmVzb2x2ZSB9IGZyb20gJ3BhdGgnO1xuXG5leHBvcnQgZGVmYXVsdCBkZWZpbmVDb25maWcoe1xuICBiYXNlOiBcIi90YWdiaXovXCIsXG4gIHBsdWdpbnM6IFtcbiAgICB2dWUoKSxcbiAgICB2dWVKc3goKSxcbiAgXSxcbiAgYnVpbGQ6IHtcbiAgICBvdXREaXI6ICdkaXN0JywgLy8gT3V0cHV0IGRpcmVjdG9yeVxuICAgIHJvbGx1cE9wdGlvbnM6IHtcbiAgICAgIGlucHV0OiByZXNvbHZlKF9fZGlybmFtZSwgJ2luZGV4Lmh0bWwnKSAvLyBFbnRyeSBwb2ludCBmb3IgdGhlIGJ1aWxkXG4gICAgfVxuICB9LFxuICByZXNvbHZlOiB7XG4gICAgYWxpYXM6IHtcbiAgICAgICdAJzogZmlsZVVSTFRvUGF0aChuZXcgVVJMKCcuL3NyYycsIGltcG9ydC5tZXRhLnVybCkpXG4gICAgfVxuICB9XG59KVxuIl0sCiAgIm1hcHBpbmdzIjogIjtBQUE2UCxTQUFTLGVBQWUsV0FBVztBQUVoUyxTQUFTLG9CQUFvQjtBQUM3QixPQUFPLFNBQVM7QUFDaEIsT0FBTyxZQUFZO0FBQ25CLFNBQVMsZUFBZTtBQUx4QixJQUFNLG1DQUFtQztBQUFpSCxJQUFNLDJDQUEyQztBQU8zTSxJQUFPLHNCQUFRLGFBQWE7QUFBQSxFQUMxQixNQUFNO0FBQUEsRUFDTixTQUFTO0FBQUEsSUFDUCxJQUFJO0FBQUEsSUFDSixPQUFPO0FBQUEsRUFDVDtBQUFBLEVBQ0EsT0FBTztBQUFBLElBQ0wsUUFBUTtBQUFBO0FBQUEsSUFDUixlQUFlO0FBQUEsTUFDYixPQUFPLFFBQVEsa0NBQVcsWUFBWTtBQUFBO0FBQUEsSUFDeEM7QUFBQSxFQUNGO0FBQUEsRUFDQSxTQUFTO0FBQUEsSUFDUCxPQUFPO0FBQUEsTUFDTCxLQUFLLGNBQWMsSUFBSSxJQUFJLFNBQVMsd0NBQWUsQ0FBQztBQUFBLElBQ3REO0FBQUEsRUFDRjtBQUNGLENBQUM7IiwKICAibmFtZXMiOiBbXQp9Cg==
