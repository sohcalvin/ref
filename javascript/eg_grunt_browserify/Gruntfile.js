module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    clean: ['dist', ],
    browserify: {
      csoh1: {
        src: 'csoh_dependency/**',
        dest: 'dist/bundle.js'
      }
    }



  });


  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-browserify');


  // Default task(s).
  grunt.registerTask('default', ['clean', 'browserify']);


};
