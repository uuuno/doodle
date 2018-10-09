// webpack.config.js
module.exports = {
    entry: './src/index.js',
    output: {
        filename: 'bundle.js',
        path: `${__dirname}/dist`,
    },
    module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
      },
      {
        test: /\.js$/,
        loader: 'babel-loader?presets=es2015',
      },
    ]
    },
    resolve: {
	extensions: ['.js', '.vue'],
	alias: {
	    vue$: 'vue/dist/vue.esm.js',
	},
    },
    devServer: {
        contentBase: 'dist',
    },
}
