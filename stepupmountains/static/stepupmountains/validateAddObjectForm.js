function isNormalInteger(str) {
	var patt = new RegExp("^[0-9]+$");
	return patt.test(str);	
}

function isNormalString(str) {
	return str!= null && str.length != 0
}

function validateAddObjectForm() {
    var isString = isNormalString(document.forms["add_object"]["object_name"].value);
    var isInt = isNormalInteger(document.forms["add_object"]["object_height"].value);
    var message = '';
    if ( ! isString ) {
	message=message.concat('Object name must be filled.\n');
    }

    if ( ! isInt ) {
	message=message.concat('Object height must be positive integer.\n');
    }

    if ( ! isString || ! isInt )
    {
        alert(message);
        return false;
    }
    return true;
}
