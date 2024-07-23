$(document).ready(function () {
  $("#sidebarToggle").on("click", function () {
    $("#sidebar").toggleClass("d-none");
    if ($("#sidebar").hasClass("d-none")) {
      $("#content").css("margin-left", "0");
    } else {
      $("#content").css("margin-left", "250px");
    }
  });

  //ajax call
  $("#paymentForm").submit(function (event) {
    event.preventDefault();

    const formData = {
      phone_number: $("input[name=phone]"),
      amount: $("input[name=amount]"),
      quantity: $("input[name=quantity]"),
      reference: $("input[name=reference]"),
      code_type: $("input[name=code_type]"),
    };
    $.ajax({
      type: "POST",
      url: "127.0.0.1:8000/",
      data: formData,
      dataType: "json",
      encode: true,
      success: function (response) {
        console.log(response);
      },
      error: function (xhr, status, error) {
        console.log(error);
      },
    });
  });
});
