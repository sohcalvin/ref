module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    uglify: {
      /* #### These is the options of grunt-contrib-uglify ####*/
      /* #### See the github readme ###*/
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      /* ###  These are subtasks which you can call with uglify:csoh1 ####*/
      csoh1: {
        files: { // I think these are standard way for specifying files for the plugins
          // See other formats as well
          'csoh1/abc.min.js': ['src/eg_grunt.js']
        }
      },
      csoh2: {
        files: {
          'csoh2/abc.min.js': ['src/eg_grunt.js']
        }
      }
    }
  });


  // Load the plugin that provides the "uglify" task.
  grunt.loadNpmTasks('grunt-contrib-uglify');

  // Default task(s).
  grunt.registerTask('default', ['uglify']); // Runs both csoh1 and csoh2
  grunt.registerTask('csoh2only', ['uglify:csoh2']); // Runs csoh2

};
