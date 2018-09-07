$(function () {
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    let items = $('ul.my_list li');
    if (items.length > 0) {
      items[items.length - 1].remove();
    }
  });
  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
