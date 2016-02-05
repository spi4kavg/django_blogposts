module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        watch: {
          scripts: {
            files: [
                'Gruntfile.js',
                'src/js/**/*.js',
                'src/sass/**/*.scss'
            ],
            tasks: ['default'],
            options: {
              debounceDelay: 250
            }
          }
        },

        compass: {
            prod: {
                options: {
                    sassDir: 'src/sass',
                    cssDir: 'vendor/css',
                    environment: 'production',
                    outputStyle: 'compressed'
                }
            },
            dev: {
                options: {
                    sassDir: 'src/sass',
                    cssDir: 'vendor/css',
                    environment: 'development',
                    outputStyle: 'expanded'
                }
            }
        },

        concat: {
            css: {
                src: [
                    'vendor/css/base.css',
                    'bower_components/bootstrap/bootstrap-3.3.6/dist/css/bootstrap.min.css',
                ],
                dest: 'vendor/blogposts.css'
            },
            js: {
                src: [
                    'bower_components/jquery/dist/jquery.min.js',
                    'bower_components/bootstrap/bootstrap-3.3.6/dist/js/bootstrap.min.js',
                ],
                dest: 'vendor/blogposts.js'
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-compass');
    grunt.loadNpmTasks('grunt-contrib-concat');

    grunt.registerTask('default', [
        "compass:dev",
        "concat:css",
        "concat:js",
    ]);

    grunt.registerTask('production', [
        "compass:prod",
        "concat:css",
        "concat:js",
    ]);

};
