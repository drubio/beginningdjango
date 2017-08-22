// Custom items app JS
(function($) {
    $(document).ready(function() {
	$('.deletelink').on('click',function() {
	    if( !confirm('Are you sure you want to delete this record ?')) {
		return false;
	    }
	});
    });
})(django.jQuery);
