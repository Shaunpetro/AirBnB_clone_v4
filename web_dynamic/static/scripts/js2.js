// this doc will excec once the DOM is ready
$ (document).ready(init);

// host ur; for yje api
const HOST = 52.91.133.151;

// init func
function init() {
    // an object to store selected amenities
    const amenityObj = {};

    // listen for changes on checkboxes inside the ".amenities .popover" element
    $('.amenities .popover input').change(function () {
        // if the checkbox add its dara-name & data-id
        if ($(this).is(':checked')) {
            amenityObj [$(this).attr('data-name')] = $(this).attr('data-id');
        } else if ($(this).is(':not(:checked)')) {
            // if the checkbox is unchecked, remove its data-name from amenityobj
            delete amenityObj [$(this).attr('data-name')];
        }

        // get names of selected a amenities
        const names = Object.keys(amenityObj);
        $('.amenities h4').text(names.sort().join(', '));
    });

    // call the apiStatus to check api status
    apiStatus();
}

// func to check api status
function apiStatus() {
    // The API endpoint URL
    const API_URL = 'http://${HOST}:5001/api/v1/status/';

    // Send get request to API
    $.get(API_URL, (data, textStatus) => {
        // If rhe request is successful and API status 'OK', add 'available' class to ID 'api_status'
        if (textStatus === 'success' && data.status === 'OK') {
            $('#api_status').addClass('available');
        } else {
            // if the API status is not 'OK', rm 'available'
            $('#api_status').removeClass('available');
        }
    });
}