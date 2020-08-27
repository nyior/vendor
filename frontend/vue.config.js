const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  publicPath: "http://127.0.0.1:8080/",
  outputDir: "./dist/",

  chainWebpack: config => {
    config
      .plugin("BundleTracker")
      .use(BundleTracker, [{ filename: "./webpack-stats.json" }]);
    config.optimization.splitChunks(false);
    config.resolve.alias.set("__STATIC__", "static");
    config.devServer
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .disableHostCheck(true)
      .headers({ "Access-Control-Allow-Origin": ["*"] });
  }
};
