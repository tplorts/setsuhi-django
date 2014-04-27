'use strict';

/* Directives */


var dmod = angular.module('workroomApp.directives', []);


dmod.directive('appVersion', ['version', function(version) {
    return function(scope, elm, attrs) {
        elm.text(version);
    };
}]);


dmod.directive('tawReorderableEntry', ['$rootScope', function($rootScope) {
    function link(scope, el, attrs, controller) {
        angular.element(el).attr("draggable", "true");
        
        var index = scope.$index;
        var id = attrs.id;

        el.bind("dragstart", function(e) {
            console.log("dstart ["+index+'] #'+id);
        });
        
        el.bind("dragend", function(e) {
            console.log('end');
        });
    }

    return {
        restrict: 'A',
        link: link
    }
}]);
