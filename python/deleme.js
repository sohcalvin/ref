var app = angular.module('myApp', ['ui.router', 'ui.bootstrap'])
.config(function ($stateProvider, $urlRouterProvider) {

  $urlRouterProvider.otherwise('/');
  $stateProvider
    .state('app', {
      url: '/',
      controller: 'AppCtrl',
      templateUrl: '/views/app.html'
    })
    .state('item', {
      url: '/profile',
      controller: 'ItemCtrl',
      templateUrl: '/views/item.html'
    });
})
.controller('AppCtrl', function($scope, $modal, $state){
  $scope.open = function(){

    // open modal whithout changing url
    $modal.open({
      templateUrl: '/views/item.html'
    });

    // I need to open popup via $state.go or something like this
  };
})
.controller('ItemCtrl', function(){});