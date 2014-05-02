'use strict';

/* Controllers */

var cmod = angular.module('workroomApp.controllers', []);

cmod.controller(
    'PictureListController', 
    ['$scope', function($scope) {

        $scope.isDragEnabled = false;
        $scope.isRepositEnabled = false;

        $scope.dragEnableChanging = function() {
            var domEntries = $('[taw-entry-draggable]');
            // If we just turned on dragging. . .
            if( $scope.isDragEnabled ) {
                $scope.isRepositEnabled = false;
                domEntries.attr('draggable','draggable');
            } else {
                domEntries.removeAttr('draggable');
            }
        };
        $scope.repositEnableChanging = function() {
            if( $scope.isRepositEnabled ) {
                $scope.isDragEnabled = false;
                var domEntries = $('[taw-entry-draggable]');
                domEntries.removeAttr('draggable');
            }
        };

        $scope.isRepositPending = false;
        $scope.pendingRepositee = null;

        $scope.beginReposit = function( iDom ) {
            $scope.pendingRepositee = parseInt(iDom);
            $scope.isRepositPending = true;

            var e = $('.taw-entry')[parseInt(iDom)];
            $(e).addClass('dragged-from');
        }

        $scope.applyReposit = function( exIDom, toIDom ) {
            $scope.moveEntry( exIDom, toIDom );

            $scope.pendingRepositee = null;
            $scope.isRepositPending = false;

            $('.dragged-from').removeClass('dragged-from');
        };

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

            // Apply this move operation
            var applyReordering = function() {
                entries[iArrayMove].fields.order_index = newOrder;
            };

            // In the drag case, I call the moveEntry function from
            // a directive's event handler, which doesn't seem to
            // encase the execution in an '$apply()'; whereas in the
            // case of a reposit, I call the moveEntry function from
            // an 'ng-click', which does seem to use '$apply()'.
            if( $scope.isRepositEnabled ) {
                applyReordering();
            } else {
                $scope.$apply( applyReordering );
            }

        }; // end: moveEntry()

    }] // end: controller function
); // end: PictureListController
