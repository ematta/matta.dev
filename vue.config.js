const path = require('path');

module.exports = {
  chainWebpack: (config) => {
    config
      .entry('app')
      .clear()
      .add('./ui/main.js')
      .end();
    config.resolve.alias
      .set('@', path.join(__dirname, './ui'));
  },
  devServer: {
    public: 'matta.dev',
    host: '0.0.0.0',
    disableHostCheck: true
  }
};
