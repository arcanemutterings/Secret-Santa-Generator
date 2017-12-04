$(function() {
	var formCounter = 3;

	//listener for '+' button
	var second = $('.second').html();
	$('.addButton').click(function() {
		if(formCounter < 50) {  //maximize number of names
			$(second).insertBefore(".third");
			$('#myForm').validator('update');
			formCounter++;
		} else {
			alert("Maximum number of people reached.");
		}
	});

	//listener for '-' button via event delegation
	$('#wrapper').on('click', '.minusButton', function(event) {
		$(event.target).parents('#extra').last().remove();
		$('#myForm').validator('update');
		formCounter--;
	});
	
	//unique form fields validation
	var validatorOptions = {
		disable: false,
		custom: {
			equals: function($el) {
				if($el.val() == false) {
					return
				}
				$el.attr('class', 'form-control skip');
				var values = [];
				var inputs = document.getElementsByTagName('input');
				var flag = false
				for (var i = 0; i < inputs.length; i++) {
					if ($el.val() == inputs[i].value && inputs[i].className != 'form-control skip'){
						flag = true;
					}
				}
				$el.attr('class', 'form-control');  
				if(flag == true) {
					return "This field has to be unique.";
				}
			}
		}
	};
	$('#myForm').validator(validatorOptions)


	//prevent santaButton from submitting
	/*$('#santaButton').click(function(event) {
    event.preventDefault();
    alert("Thanks!");
  })*/
});