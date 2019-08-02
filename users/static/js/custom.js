$(document).ready(function() {
  $('.freshmen').click(function() {
    $('.collapse-transferee').collapse('hide')
  })
  $('.transferee').click(function() {
    $('.collapse-freshmen').collapse('hide')
  })

  // ############################################################################
  $('.modal').modal('show')
});