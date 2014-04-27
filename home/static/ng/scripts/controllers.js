'use strict';

/* Controllers */

angular.module('workroomApp.controllers', [])
    .controller('PictureListController', function($scope) {
        $scope.pictureEntries = ngData_pictureEntries;
    });
