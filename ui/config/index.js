const config = {
  api: {
    domain: process.env.VUE_APP_API_DOMAIN || 'localhost',
    port: process.env.VUE_APP_API_PORT || 3000,
  },
  ui: {
    domain: process.env.VUE_APP_UI_DOMAIN || 'localhost',
    port: process.env.VUE_APP_UI_PORT || 8080,
  },
  schema: process.env.NODE_ENV === 'production' ? 'https' : 'http',
};

export default config;
