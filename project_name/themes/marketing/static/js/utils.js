var ajaxConfig = {
	callback: function(content, link, params, scripts) {
		$('.masthead .nav li > a').each(function() {
			if($(this).attr('href') == $(link).attr('href')) {
				$(this).parent('li').addClass('active');
			}
			else {
				$(this).parent('li').removeClass('active');
			}
		});
		
		if($('.ss-form-entry').length > 0) {
			$('.ss-form-entry input[type=submit]').addClass('btn btn-large btn-success');
		}
	}
};

$(function(){
	if($('.ss-form-entry').length > 0) {
		$('.ss-form-entry input[type=submit]').addClass('btn btn-large btn-success');
	}
});