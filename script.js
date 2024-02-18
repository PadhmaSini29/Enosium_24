$(document).ready(function() {
    $('#contentForm').submit(function(e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/summarize',
            data: $('#contentForm').serialize(),
            success: function(response) {
                $('#summary').html('<h2>Summary</h2><p>' + response + '</p>');
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
