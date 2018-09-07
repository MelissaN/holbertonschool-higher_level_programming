$(function () {
  $('#add_item').click(function () {
    $('ul.my_list').append($("<li></li>").text("Item"));
  });
});
