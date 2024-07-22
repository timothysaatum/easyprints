$(document).ready(function () {
  $("#sidebarToggle").on("click", function () {
    $("#sidebar").toggleClass("d-none");
    if ($("#sidebar").hasClass("d-none")) {
      $("#content").css("margin-left", "0");
    } else {
      $("#content").css("margin-left", "250px");
    }
  });
});
