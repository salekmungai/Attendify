$(document).ready(function () {
  // Show modal when "Register Now" is clicked
  $('#openModal').click(function () {
    $('#eventModal').removeClass('hidden');
  });

  // Hide modal when "x" is clicked
  $('#closeModal').click(function () {
    $('#eventModal').addClass('hidden');
  });

  // Optional: hide modal when clicking outside of it
  $(window).click(function (event) {
    if ($(event.target).is('#eventModal')) {
      $('#eventModal').addClass('hidden');
    }
  });
});
