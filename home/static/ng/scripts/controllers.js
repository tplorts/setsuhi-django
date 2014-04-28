'use strict';

/* Controllers */

var cmod = angular.module('workroomApp.controllers', []);

cmod.controller(
    'PictureListController', 
    ['$scope', function($scope) {
        $scope.pictureEntries = ngData_pictureEntries;
        var entries = $scope.pictureEntries;
        for( var i=0; i < entries.length; i++ )
            entries[i]['arrayIndex'] = i;

        $scope.moveEntry = function( fromIndex, toIndex ) {
            if( fromIndex != toIndex ) {
                console.log('move from ' + fromIndex + ' to ' + toIndex);
                $scope.$apply(function() {
                    var eFrom = entries[fromIndex];
                    var eTo = entries[toIndex];
                    var oi = eFrom.fields.order_index;
                    eFrom.fields.order_index = eTo.fields.order_index;
                    eTo.fields.order_index = oi;
                });
            }
        };
    }]
);
