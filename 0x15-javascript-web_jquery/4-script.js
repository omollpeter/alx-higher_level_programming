$('div#toggle_header').click(function () {
  $(this).toggleClass(function () {
    // Do this if there is no initial class
    return $(this).is('.red, .green') ? 'red green' : 'red';
  });
});
