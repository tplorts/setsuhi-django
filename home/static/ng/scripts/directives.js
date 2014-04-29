'use strict';

/* Directives */


var dmod = angular.module('workroomApp.directives', []);


dmod.directive('appVersion', ['version', function(version) {
    return function(scope, elm, attrs) {
        elm.text(version);
    };
}]);

var priorOver = null;

function linkDrag(scope, el, attrs) {
    var ngel = angular.element(el);
    ngel.attr("draggable", "true");
    ngel.addClass('entry-row');

    var thisIndex = attrs.index;

    el.bind("dragstart", function(eve) {
        var e = eve.originalEvent;
        var dt = e.dataTransfer;
        ngel.addClass('dragged-from');
        dt.effectAllowed = 'move';
        console.log('starting '+thisIndex);
        dt.setData("text/plain", thisIndex);
    });

    el.bind("dragend", function(e) {
        ngel.removeClass('dragged-from');
        priorOver = null;
        e.originalEvent.dataTransfer.clearData();
    });
}


function linkDrop(scope, el, attrs) {
    var ngel = angular.element(el);
    ngel.addClass('drop-zone');

    var thisIndex = attrs.index;


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
        if( thisIndex != priorOver ) {
            priorOver = thisIndex;
            var i = dt.getData("text/plain");
            if( i != thisIndex ) {
                ngel.addClass('dragged-over');
            }
        }
    });
    
    el.bind("dragleave", function(eve) {
        ngel.removeClass('dragged-over');
        priorOver = null;
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


dmod.directive('tawDraggableEntry', function() {
    return {
        restrict: 'A',
        link: linkDrag
    }
});


dmod.directive('tawEntryDropZone', function() {
    return {
        restrict: 'A',
        link: linkDrop,
        scope: {
            onDrop: '&'
        }
    }
});

