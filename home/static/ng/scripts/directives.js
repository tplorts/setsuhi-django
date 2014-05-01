'use strict';

/* Directives */


var dmod = angular.module('workroomApp.directives', []);


dmod.directive('appVersion', ['version', function(version) {
    return function(scope, elm, attrs) {
        elm.text(version);
    };
}]);


function linkDrag(scope, el, attrs) {
    var ngel = angular.element(el);

    el.bind("dragstart", function(eve) {
        var e = eve.originalEvent;
        var dt = e.dataTransfer;
        ngel.addClass('dragged-from');
        dt.effectAllowed = 'move';
        var thisIndex = $(e.target).attr('data-i-dom');
        dt.setData("text/plain", thisIndex);
    });

    el.bind("dragend", function(e) {
        ngel.removeClass('dragged-from');
        e.originalEvent.dataTransfer.clearData();
    });
}


function linkDrop(scope, el, attrs) {
    var ngel = angular.element(el);
    ngel.addClass('drop-zone');

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
        ngel.addClass('dragged-over');
    });
    
    el.bind("dragleave", function(eve) {
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
        var oldIndex = parseInt( dt.getData("text/plain") );
        var thisIndex = parseInt( $(e.target).attr('data-i-dom') );
        scope.onDrop({
            exIDom: oldIndex, 
            toIDom: thisIndex
        });
        
        return false;
    });
}


dmod.directive('tawEntryDraggable', function() {
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

