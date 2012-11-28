function fix_tabindexes() {
    /* meddle with recaptcha tab indexes */
    $("#recaptcha_response_field").attr('tabindex', 0);
    $("#spam_submit").attr('tabindex', 1);
    $("#recaptcha_reload_btn").attr('tabindex', 2);
    $("#recaptcha_switch_audio_btn").attr('tabindex', 3);
    $("#recaptcha_whatsthis_btn").attr('tabindex', 4);
}


$(document).ready(function() {
    /* dramatically reveal ReCaptcha and fix tab indexes */
    $("#recaptcha_parent").show("fast");
    fix_tabindexes();
});


function new_recaptcha(){
    /* render a new recaptcha when the form is re-rendered via AJAX */
    Recaptcha.create(
        $RECAPTCHA_PUBLIC_KEY,
        "recaptcha",
        {
            theme: "clean",
            tabindex: 0,
            callback: function(){
                $("#recaptcha_parent").show("slow");
                fix_tabindexes();
            }
        }
    );
}


$("#SpammerForm").submit(function(event) {
    /* stop form from submitting normally */
    event.preventDefault();
    /* get some values from elements on the page */
    $('#recaptcha_parent').toggle("fast");
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
            // only clear the address field if there are no errors
            if ($("#errors").length !== 0) {
                $form.find('input[name="address"]').focus();
            }
            else {
                $form.find('input[name="address"]').val("").focus();
            }
            $form.find('input[name="address"]').focus();
            $("#thanks").delay(10000).fadeOut(750);
            $("#errors").delay(10000).fadeOut(750);
            new_recaptcha();
        }
    );
});
