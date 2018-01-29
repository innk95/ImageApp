$(document).ready(function(){
    var width = $('#width');
    var height = $('#height');
    var size = $('#size');
    var image = $('#image');
    $('#btn').click(function(){
        image.css('width', width.val());
         image.css('height', height.val());
        image.css('size', size.val());
    })
})
