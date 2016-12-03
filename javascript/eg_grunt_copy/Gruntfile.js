module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    clean: ['dest', ],
    copy: {
      csoh1: {
        files: [
          // includes files within path
          {
            expand: true,
            src: ['from/**'],
            dest: 'dest/',
            filter: 'isFile'
          }


        ],
      },

    }
  });


  // Load the plugin that provides the "uglify" task.
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-clean');


  // Default task(s).
  grunt.registerTask('default', ['clean', 'copy:csoh1']);


};
