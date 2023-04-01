
const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/static/'
    : "http://10.30.66.49:8080",
  outputDir: "./dist/",

  configureWebpack: {
    plugins: [
      new BundleTracker({ filename: "./webpack-stats.json" }),
    ],
    output: {
      filename: "bundle.js",
    },
    optimization: {
      splitChunks: false,
    },
    resolve: {
      alias: {
        __STATIC__: "static",
      },
    },
    devServer: {
      host: "127.0.0.1",
      port: 8080,
      hot: "only",
      https: false,
      allowedHosts: "auto",
      headers: { "Access-Control-Allow-Origin": ["*"] },
    },
  },

  css: {
    extract: {
      filename: 'bundle.css',
      chunkFilename: 'bundle.css',
    },
  }
};
