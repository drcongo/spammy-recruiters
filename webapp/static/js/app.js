function fix_tabindexes() {
    // meddle with recaptcha tab indexes
    $("#recaptcha_response_field").attr('tabindex', 0)
        .attr("required", "required");
    $("#spam_submit").attr('tabindex', 1);
    $("#recaptcha_reload_btn").attr('tabindex', 2);
    $("#recaptcha_switch_audio_btn").attr('tabindex', 3);
    $("#recaptcha_whatsthis_btn").attr('tabindex', 4);
    $("#ghlink").attr('tabindex', 5);
}

$(document).ready(function() {
    // dramatically reveal recaptcha, and fix tab indexes
    $("#recaptcha_parent").hide().slideDown("slow");
    fix_tabindexes();
});

$(window).bind("load", function() {
    // do this stuff after the page has fully rendered
    get_updates();
});

function new_recaptcha(){
    // render a new recaptcha when the form is re-populated via AJAX
    $("#recaptcha_parent").hide().delay(250).slideDown("slow");
    Recaptcha.create(
        $RECAPTCHA_PUBLIC_KEY,
        "recaptcha",
        {
            theme: "clean",
            tabindex: 0,
            callback: function(){
                fix_tabindexes();
                get_updates();
            }
        }
    );
}

$("#SpammerForm").submit(function(event) {
    event.preventDefault();
    var $form = $(this);
    // get "successful" form values and URL
    values = $form.serializeArray();
    url = $form.attr('action');
    $('#recaptcha_parent').slideUp("slow", function(){
            // send the data using POST and re-populate the form w/the results
            $.post(
                url,
                values,
                function(data) {
                    // TODO we need some 500 error handling here
                    // re-populate the form
                    $form.html($(data));
                    $(".information").hide().fadeIn(300);
                    // only clear the address field if there are no errors
                    if ($("#errors").length !== 0) {
                        $form.find('input[name="address"]').focus();
                    }
                    else {
                        $form.find('input[name="address"]').val("").focus();
                        $(".bodycopy").fadeTo("fast", 1.0);
                    }
                    $(".information").delay(7500).animate({
                        height: "toggle", opacity: "toggle"
                        }, "slow" );
                    new_recaptcha();
                }
            );
    });
});

function get_updates() {
    // get latest query counts and last updated time
    $('#last-updated').parent().hide("slow", function(){
            $.get('updates', function(data) {
                var keys = Object.keys(data);
                $('#count').hide().text(data.count).fadeTo('slow', 1.0);
                $('#last-updated').text(
                    "The spammer address file was last checked for updates " +
                    data.last_updated + ".").parent().fadeTo('slow', 1.0);
        });
    });
}

$("#address").keyup(function(){
    // show or fade body copy and GitHub link based on address input
    if ($(this).val()) {
        $(".bodycopy").fadeTo("slow", 0.5);
    }
    else {
        $(".bodycopy").fadeTo("fast", 1.0);
    }
});
