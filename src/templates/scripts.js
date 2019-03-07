$("button").click(function(e) {
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: "src/songs.py",
        data: {
            id: $(this).val(), // < note use of 'this' here
        },
        success: function(result) {
            alert('ok');
        },
        error: function(result) {
            alert('error');
        }
    });
});