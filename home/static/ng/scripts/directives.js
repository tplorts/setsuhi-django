'use strict';

/* Directives */


var dmod = angular.module('workroomApp.directives', []);


dmod.directive('appVersion', ['version', function(version) {
    return function(scope, elm, attrs) {
        elm.text(version);
    };
}]);

var priorEntrance = null;

dmod.directive('tawReorderableEntry', ['$rootScope', function($rootScope) {
    function link(scope, el, attrs, controller) {
        var ngel = angular.element(el);
        ngel.attr("draggable", "true");

        var thisIndex = attrs.index;

        el.bind("dragstart", function(eve) {
            var e = eve.originalEvent;
            var dt = e.dataTransfer;
            ngel.addClass('dragged-from');
            dt.effectAllowed = 'move';
            dt.setData("text/plain", thisIndex);
        });

        el.bind("dragend", function(e) {
            ngel.removeClass('dragged-from');
            priorEntrance = null;
        });



        el.bind("dragover", function(eve) {
            var e = eve.originalEvent;
            var dt = e.dataTransfer;
            if (e.preventDefault) {
                // Necessary. Allows us to drop.
                e.preventDefault();
            }
            dt.dropEffect = 'move';
            return false;
        });

        el.bind("dragenter", function(eve) {
            var e = eve.originalEvent;
            var dt = e.dataTransfer;
            if( thisIndex != priorEntrance ) {
                priorEntrance = thisIndex;
                var sourceIndex = dt.getData('text/plain');
                if( sourceIndex != thisIndex ) {
                    ngel.addClass('dragged-over');
                }
            }
        });
        
        el.bind("dragleave", function(eve) {
            var e = eve.originalEvent;
            ngel.removeClass('dragged-over');
        });

        el.bind("drop", function(eve) {
            var e = eve.originalEvent;
            var dt = e.dataTransfer;
            if (e.stopPropagation) {
                // Stops some browsers from redirecting.
                e.stopPropagation();
            }
            ngel.removeClass('dragged-over');
            var oldIndex = dt.getData("text/plain");
            if( thisIndex != oldIndex ) {
                scope.onDrop({
                    fromIndex: oldIndex, 
                    toIndex: thisIndex
                });
            }
            return false;
        });

    }

    return {
        restrict: 'A',
        link: link,
        scope: {
            onDrop: '&'
        }
    }
}]);
