'use strict';

/* Controllers */

var cmod = angular.module('workroomApp.controllers', []);

cmod.controller(
    'PictureListController', 
    ['$scope', function($scope) {
        $scope.pictureEntries = ngData_pictureEntries;
        var entries = $scope.pictureEntries;
        var qEntries = entries.length;

        for( var i=0; i < qEntries; i++ )
            entries[i]['arrayIndex'] = i;

        // exIDom: the DOM index of the element to move
        // toIDom: the DOM index to which the element is moving
        $scope.moveEntry = function( exIDom, toIDom ) {

            // Ignore the inconsequential cases:
            //   - moving to the same place
            //   - moving to the immediately following place
            if( toIDom == exIDom  ||
                toIDom == exIDom + 1 ) return;

            var domEntries = $('.taw-entry');

            var iArrayAt = function( domIndex ) {
                var domEntry = $(domEntries[domIndex]);
                return parseInt(domEntry.attr('data-i-array'));
            };

            // Return the order value for the entry identified
            // by its present DOM position.  If domIndex is
            // out of bounds, return 2 more in the respective
            // direction.
            var orderValueAt = function( domIndex ) {
                var more = 0;
                if( domIndex < 0 ) {
                    more = -2;
                    domIndex = 0;
                } else if( domIndex >= qEntries ) {
                    more = 2;
                    domIndex = qEntries - 1;
                }
                var iA = iArrayAt( domIndex );
                return entries[iA].fields.order_index + more;
            };

            // Put the new order value between the two
            // new neighbors of the moving element.
            var orderAfter = orderValueAt( toIDom );
            var orderBefore = orderValueAt( toIDom - 1 );
            var newOrder = (orderAfter + orderBefore) / 2;

            // Locate the data of the entry to move
            var iArrayMove = iArrayAt( exIDom );

            // Apply this move operation while Angular is watching
            $scope.$apply(function() {
                entries[iArrayMove].fields.order_index = newOrder;
            });

        }; // end: moveEntry()
    }] // end: controller function
); // end: PictureListController
