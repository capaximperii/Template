module.exports = {
  chainWebpack: config => {
    config.plugin("html").tap(args => {
      args[0].title = process.env.title;
      return args;
    }),
      config.module
        .rule("raw")
        .test(/\.md$/)
        .use("raw-loader")
        .loader("raw-loader")
        .end();
  },
  transpileDependencies: ["vuetify"],
  outputDir: "../backend/Ui"
};
