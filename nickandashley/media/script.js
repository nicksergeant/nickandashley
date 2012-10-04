$(function() {
    if ($("#nav").length) {
        var activeNav = $("#nav").find('.active');
        $("#nav a").click(function() {
            activeNav.removeClass('active');
            $(this).addClass('active');
        });
    }
    
    if ($(".wedding-party").length) {
        maxWidth = 300;
        minWidth = 123;

        $("#banner-set-1 a").hover(
            function(){
                if (!$(this).hasClass("active")) {
                    $(lastBlock1)
        	            .attr('class','')
                        .animate({width: minWidth+"px"}, { queue:false, duration:400 })
        	            .find('p img')
        	                .animate({marginLeft: "-51px"}, { queue:false, duration:400})
        	            .end()
        	            .find('p span')
        	                .fadeOut(400);
        	        $(this)
        	            .attr('class', 'active')
        	            .animate({width: maxWidth+"px"}, { queue:false, duration:400})
        	            .find('p img')
        	                .animate({marginLeft: "0"}, { queue:false, duration:400})
        	            .end()
         	            .find('p span')
         	                .fadeIn(400);
        	        lastBlock1 = this;
                }
            }
        );
        lastBlock1 = $("#a1");
        
        $("#banner-set-2 a").hover(
            function(){
                if (!$(this).hasClass("active")) {
                    $(lastBlock2)
        	            .attr('class','')
                        .animate({width: minWidth+"px"}, { queue:false, duration:400 })
        	            .find('p img')
        	                .animate({marginLeft: "-51px"}, { queue:false, duration:400})
        	            .end()
        	            .find('p span')
        	                .fadeOut(400);
        	        $(this)
        	            .attr('class', 'active')
        	            .animate({width: maxWidth+"px"}, { queue:false, duration:400})
        	            .find('p img')
        	                .animate({marginLeft: "0"}, { queue:false, duration:400})
        	            .end()
         	            .find('p span')
         	                .fadeIn(400);
        	        lastBlock2 = this;
                }
            }
        );
        lastBlock2 = $("#a2");
    }
    
    $("#contact-us").colorbox({
        inline: true,
        height: 420,
        href: "#contact-us-content",
        transition: "none",
        width: 600
    });
    
    $(".entree-options").colorbox({
        inline: true,
        height: 585,
        href: "#entree-options-content",
        transition: "none",
        width: 600
    });

    if ($("#add-comment").length) {
        $("#add-comment").bind('click', function() {
            $("li.add-comment").slideToggle();
            return false;
        });
        
        $('#name, #comment').focus(function() {
            if ($(this).data('orig') == undefined) {
                $(this).data('orig', $(this).attr('value'));
                $(this).attr('value', '');
            } else if ($(this).data('orig') == $(this).attr('value')) {
                $(this).attr('value', '');
            }
        });
        $('#name, #comment').blur(function() {
            if ($(this).attr('value') == '') {
                $(this).attr('value', $(this).data('orig'));
            }
        });
        
        $("#add-comment-form").bind('submit', function() {
            if (($('#name').val() != '') && ($('#name').val() != 'Your name') && ($('#comment').val() != '') && ($('#comment').val() != 'Your comment')) {
                $("#comment-modal").toggle();
                $.post('/guestbook/post/',
                    {
                        'name': $("#name").val(),
                        'comment': $("#comment").val()
                    },
                    function(data) {
                        $("li.add-comment").after('' +
                            '<li class="group disabled" id="comment-' + data.id + '">' +
                            '    <dt style="color: green;">' +
                            '        ' + data.name +
                            '        <span>' + data.created + '</span>' +
                            '    </dt>' +
                            '    <dd>' +
                            '        ' + data.comment +
                            '    </dd>' +
                            '</li>');
                            $("#comment-modal").toggle();
                        $("#comment-" + data.id ).slideToggle();
                        $("li.add-comment").slideToggle();
                    },
                    'json');
            } 
            return false;
        });
    }
    
    $("#contact-form").bind('submit', function() {
        if (($('#name').val() != '') && ($('#email').val() != '') && ($('#message').val() != '')) {
            $("#contact-modal").toggle();
            $.post('/contact-us/post/',
                {
                    'name': $("#name").val(),
                    'email': $("#email").val(),
                    'message': $("#message").val(),
                    'human': $("#human").val()
                },
                function(data) {
                    $("#contact-form").html("<p style='color: green;'>Thanks! We've received your message, and will get back to you ASAP.");
                    $("#contact-modal").toggle();
                },
                'json');
        } 
        return false;
    });
    if ($(".rsvp").length) {
        $("#id_number_of_guests option[value='0']").remove();
        $("#id_attending").change(function() {
            if ($(this).val() == 'N') {
                $("#guest-1-first-name, #guest-1-last-name").hide();
                $(".attending").after($("#guest-1-first-name"));
                $("#guest-1-first-name").after($("#guest-1-last-name"));
                $("#guest-1-first-name, #guest-1-last-name").addClass('group');
                $("#guest-1-first-name label").text("Your first name:");
                $("#guest-1-last-name label").text("Your last name:");
                $(".number_of_guests, .your-email, #submit, .guests, .your-phone, #guest-1, #guest-2, #guest-3, #guest-4").hide();
                $(".your-email, .your-phone, your-first-name, .your-last-name, #submit, #guest-1-first-name, #guest-1-last-name").fadeIn('fast');
            } else if ($(this).val() == 'Y') {
                $("#guest-1 .legend").after($("#guest-1-first-name"));
                $("#guest-1-first-name").after($("#guest-1-last-name"));
                $("#guest-1-first-name, #guest-1-last-name").removeClass('group');
                $("#guest-1-first-name label").text("First name");
                $("#guest-1-last-name label").text("Last name");
                $("#id_number_of_guests").val('');
                $("#guest-1, #guest-2, #guest-3, #guest-4, .guests, #submit").hide();
                $(".number_of_guests, .your-email, .your-phone").fadeIn('fast');
            }
            return false;
        });
        $("#id_number_of_guests").change(function() {
            $(".guests").show();
            if ($(this).val() == '1') {
                $("#guest-1, #guest-2, #guest-3, #guest-4").hide();
                $("#guest-1, #submit").fadeIn('fast');
            } else if ($(this).val() == '2') {
                $("#guest-1, #guest-2, #guest-3, #guest-4").hide();
                $("#guest-1, #guest-2, #submit").fadeIn('fast');
            } else if ($(this).val() == '3') {
                $("#guest-1, #guest-2, #guest-3, #guest-4").hide();
                $("#guest-1, #guest-2, #guest-3, #submit").fadeIn('fast');
            } else if ($(this).val() == '4') {
                $("#guest-1, #guest-2, #guest-3, #guest-4").hide();
                $("#guest-1, #guest-2, #guest-3, #guest-4, #submit").fadeIn('fast');
            }
            return false;
        });
        if (submitted==true) {
            $(".your-phone, .your-email, .guests, .number_of_guests, #guest-1, #guest-2, #guest-3, #guest-4, #submit").show();
            if ($("#id_attending").val() == 'N') {
                $(".attending").after($("#guest-1-first-name"));
                $("#guest-1-first-name").after($("#guest-1-last-name"));
                $("#guest-1-first-name, #guest-1-last-name").addClass('group');
                $("#guest-1-first-name label").text("Your first name:");
                $("#guest-1-last-name label").text("Your last name:");
                $(".number_of_guests, .your-email, #submit, .guests, .your-phone, #guest-1, #guest-2, #guest-3, #guest-4").hide();
                $(".your-email, .your-phone, your-first-name, .your-last-name, #submit, #guest-1-first-name, #guest-1-last-name").show();
            };
        };
    };
})
