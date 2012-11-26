$(document).ready(function() {
    $("#recaptcha_parent").show("slow");
    $("#recaptcha_response_field").attr('tabindex', 0);
    $("#recaptcha_reload_btn").attr('tabindex', 1);
    $("#recaptcha_switch_audio_btn").attr('tabindex', 2);
    $("#recaptcha_whatsthis_btn").attr('tabindex', 3);
});


function new_recaptcha(){
    /* render a new recaptcha when the form is re-rendered via AJAX */
    $('#recaptcha_parent').toggle();
    Recaptcha.create("6LdLmtkSAAAAAMhQTQOq2zRvnSLeVDyLESrd59Kb",
    "recaptcha",
    {
        theme: "clean",
        tabindex: 1,
        callback: function(){$("#recaptcha_parent").show("slow");}
    }
    );
}


$("#SpammerForm").submit(function(event) {
    /* stop form from submitting normally */
    event.preventDefault();
    /* get some values from elements on the page */
    var $form = $(this),
    address = $form.find('input[name="address"]').val(),
    csrf = $form.find('input[name="csrf_token"]').val(),
    recaptcha_r = $form.find('input[name="recaptcha_response_field"]').val(),
    recaptcha_c = $form.find('input[name="recaptcha_challenge_field"]').val(),
    url = $form.attr('action');
    /* send the data using POST and re-generate the form w/the results */
    $.post(url, {
        address: address,
        csrf_token: csrf,
        recaptcha_response_field: recaptcha_r,
        recaptcha_challenge_field: recaptcha_c
        },
        function(data) {
            var content = $(data);
            $("#SpammerForm").html(content);
            $form.find('input[name="address"]').val("").focus();
            $("#thanks").delay(5000).fadeOut(500);
            $("#errors").delay(10000).fadeOut(750);
            new_recaptcha();
        }
    );
});
