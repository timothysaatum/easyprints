$(document).ready(
  function () {
    $("#sidebarToggle").on("click", function () {
      $("#sidebar").toggleClass("d-none");
      if ($("#sidebar").hasClass("d-none")) {
        $("#content").css("margin-left", "0");
      } else {
        $("#content").css("margin-left", "250px");
      }
    });
  },
  function submitForm() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    // Perform your form submission logic here
    console.log("Form submitted:", { name, email, message });

    // Close the modal after submission
    const modal = bootstrap.Modal.getInstance(
      document.getElementById("exampleModal")
    );
    modal.hide();
  }
);
