$(document).ready(function () {
  function updateDisplay() {
    const currencySymbol = 'GHS';
    var inputValue = parseFloat($("#id_quantity").val()) || 0;
    var codeType = $("#id_code_type").val();
    var multiplier = 1;

    if (codeType === 'WASSCE') {
      multiplier = 15;
    } else if (codeType === 'BECE') {
      multiplier = 10;
    } else if (codeType === 'SHS PLACEMENT CODES') {
      multiplier = 20;
    }
    var result = inputValue * multiplier
    console.log(multiplier);
    $("#totalPrice").text(currencySymbol + result.toFixed(2));
  }
  $('#id_quantity').on('input', updateDisplay);
  $("#id_code_type").on("input", updateDisplay);
});