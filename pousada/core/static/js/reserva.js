let urlcheckout;

$('.fazerCheckout').on('click', function(event) {
  event.preventDefault();
  let url = $(this).data('url');
  urlcheckout = $(this).data('urlcheckout');
  $.ajax({
    url: url,
    success: function(response) {
      item = response.data[0]
      $('#id_checkout_pk').val(item.pk);
      $('#saldo-devedor').html(item.valor_diaria);
      $('#id_checkout_valor_diaria').val(item.valor_diaria);
    },
    error: function(xhr) {
      // body... xhr.statusText + xhr.responseText
    }
  })
});

$('#salvarCheckout').on('click', function() {
  $.ajax({
    url: urlcheckout,
    type: 'POST',
    data: {
      id: $('#id_checkout_pk').val(),
      valor_diaria: $('#id_checkout_valor_diaria').val()
    },
    success: function(response) {
      location.reload();
    },
    error: function(xhr) {
      // body... xhr.statusText + xhr.responseText
    }
  })
});