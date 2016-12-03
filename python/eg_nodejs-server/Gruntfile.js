// Generated on 2016-01-30 using generator-angular 0.15.1
'use strict';

module.exports = function (grunt) {

  // Time how long tasks take. Can help when optimizing build times
  require('time-grunt')(grunt);

  // Automatically load required Grunt tasks
  require('jit-grunt')(grunt, {});

  grunt.loadNpmTasks('grunt-connect-proxy');

  // Configurable paths for the application
  var appConfig = {
    dist: 'dist'
  };

//  var proxyServer = {
//    middleware: function (connect) {
//      return [
//        require('grunt-connect-proxy/lib/utils').proxyRequest,
//        connect.static('.tmp'),
//        connect().use(
//          '/bower_components',
//          connect.static('./bower_components')
//        ),
//        connect().use(
//          '/app/styles',
//          connect.static('./app/styles')
//        ),
//        connect.static(appConfig.app)
//      ];
//    },
//    setting: [{
//      context: '/cvr',
//      host: 'localhost',
//      port: 5000,
//      https: false,
//      xforward: false,
//      hideHeaders: ['x-removed-header']
//    }]
//  };

  var proxyServerDist = {
    middleware: function (connect) {
      return [
        require('grunt-connect-proxy/lib/utils').proxyRequest,
        connect.static(appConfig.dist)
      ];
    },
    setting: [{
      context: '/cvr',
      host: 'localhost',
      port: 5000,
      https: true,
      xforward: false,
      hideHeaders: ['x-removed-header']
    }]
  };

  // Define the configuration for all the tasks
  grunt.initConfig({

    // Project settings
    yeoman: appConfig,

    // The actual grunt server settings
    connect: {
//      proxies: proxyServer.setting,
      options: {
        port: 9000,
        hostname: '0.0.0.0'
      },
      dist: {
        options: function(){
          try {
            var opt = {
              open: true,
              base: '<%= yeoman.dist %>',
              middleware: proxyServerDist.middleware,
              protocol: 'https',
              key: grunt.file.read('/production-server/release/cert/server.key').toString(),
              cert: grunt.file.read('/production-server/release/cert/server.crt').toString()
            };
            return opt;
          }catch(e){
            return {
              open: true,
              base: '<%= yeoman.dist %>',
              middleware: proxyServerDist.middleware
            }
          }
        }(),
        appendProxies : false,
        proxies: proxyServerDist.setting
      }
    },
  });

  grunt.registerTask('serve', 'Compile then start a connect web server', function (target) {
    if (target === 'static') {
      return  grunt.task.run([
            'configureProxies:dist',
             'connect:dist:keepalive'
             ]);
    }
  });

  grunt.registerTask('default', [
    'newer:jshint',
    'newer:jscs',
    'test',
    'build'
  ]);
};
