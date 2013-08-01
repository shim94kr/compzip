$.ready(function(){
    $("#login").click(function() {
        var url = "{% url 'login' %}"; // the script where you handle the form input.
        $.ajax({
               type: "POST",
               url: url,
               data: $("#login_form").serialize(), // serializes the form's elements.
               success: function(data)
               {
                   $("#login_form").hide();
                   $("#afterlogin").append("hello"+data['first_name']);
                   // show response from the php script.
               }
        });
        return false; // avoid to execute the actual submit of the form.
    });
});