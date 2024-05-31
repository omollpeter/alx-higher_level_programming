$(function () {
  $('input#btn_translate').click(function () {
    const code = $('input#language_code').prop('value');

    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + code, function (data, textStatus) {
      $('div#hello').text(data.hello);
    });
  });
});
