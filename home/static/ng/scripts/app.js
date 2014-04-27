'use strict';


// Declare app level module which depends on filters, and services
var workroomApp = angular.module('workroomApp', [
  'ngRoute',
  'workroomApp.filters',
  'workroomApp.services',
  'workroomApp.directives',
  'workroomApp.controllers'
]).config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
}]);
