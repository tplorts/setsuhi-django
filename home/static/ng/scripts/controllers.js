'use strict';

/* Controllers */

var cmod = angular.module('workroomApp.controllers', []);

cmod.controller(
    'PictureListController', 
    ['$scope', function($scope) {

        $scope.pictureEntries = ngData_pictureEntries;
        $scope.originalEntries = deepCopy( $scope.pictureEntries );

        var entries = $scope.pictureEntries;
        var qEntries = entries.length;

        $scope.isDragEnabled = false;
        $scope.isRepositEnabled = false;

        $scope.isRepositPending = false;
        $scope.pendingRepositee = null;

        // Give each entry its index for access in
        // this array.  Used later in DOM.
        for( var i=0; i < qEntries; i++ )
            entries[i]['arrayIndex'] = i;


        $scope.dragEnableChanging = function() {
            var domEntries = $('[taw-entry-draggable]');
            // If we just turned on dragging. . .
            if( $scope.isDragEnabled ) {
                $scope.isRepositEnabled = false;
                $scope.endReposit();
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
            } else {
                $scope.endReposit();
            }
        };


        $scope.beginReposit = function( iDom ) {
            $scope.pendingRepositee = parseInt(iDom);
            $scope.isRepositPending = true;

            var e = $('.taw-entry')[parseInt(iDom)];
            $(e).addClass('pending-entry');
        }

        $scope.endReposit = function() {
            $scope.pendingRepositee = null;
            $scope.isRepositPending = false;
            $('.pending-entry').removeClass('pending-entry');
        };            

        $scope.applyReposit = function( exIDom, toIDom ) {
            $scope.moveEntry( exIDom, toIDom );
            $scope.endReposit();
        };



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

            // Return the rank value for the entry identified
            // by its present DOM position.  If domIndex is
            // out of bounds, return 2 more in the respective
            // direction.
            var rankAt = function( domIndex ) {
                var more = 0;
                if( domIndex < 0 ) {
                    more = -2;
                    domIndex = 0;
                } else if( domIndex >= qEntries ) {
                    more = 2;
                    domIndex = qEntries - 1;
                }
                var iA = iArrayAt( domIndex );
                return entries[iA].fields.rank + more;
            };

            // Put the new rank value between the two
            // new neighbors of the moving element.
            var rankAfter = rankAt( toIDom );
            var rankBefore = rankAt( toIDom - 1 );
            var newRank = (rankAfter + rankBefore) / 2;

            // Locate the data of the entry to move
            var iArrayMove = iArrayAt( exIDom );

            // Apply this move operation
            var applyReranking = function() {
                entries[iArrayMove].fields.rank = newRank;
            };

            // In the drag case, I call the moveEntry function from
            // a directive's event handler, which doesn't seem to
            // encase the execution in an '$apply()'; whereas in the
            // case of a reposit, I call the moveEntry function from
            // an 'ng-click', which does seem to use '$apply()'.
            if( $scope.isRepositEnabled ) {
                applyReranking();
            } else {
                $scope.$apply( applyReranking );
            }

        }; // end: moveEntry()

        $scope.saveChanges = function() {

            // Before committing to an update, check whether
            // any modifications exist.
            var changedEntries = [];
            for( var i=0; i<qEntries; i++ ) {
                var o1 = entries[i];
                var o2 = $scope.originalEntries[i];
                var s1 = JSON.stringify(o1.fields);
                var s2 = JSON.stringify(o2.fields);
                if( s1 != s2 ) {
                    changedEntries.push( o1 );
                }
            }

            if( changedEntries.length == 0 ) {
                $scope.flashMessage('There are no changes.');
            } else {
                var entriesJSON = JSON.stringify( changedEntries );
                //TODO: send to backend
            }
        };

        $scope.flashMessage = function( msg ) {
            var board = $('.message-board');
            var hideMessage = function() {
                board.removeClass('showing');
            };
            board.find('.message').html( msg );
            board.addClass('showing');
            setTimeout( hideMessage, 2500 );
        }

    }] // end: controller function
); // end: PictureListController
