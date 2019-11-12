let id;

function clearForms() {
  $(':input').not(':button, :submit, :reset, :hidden, :checkbox, :radio').val('');
  $(':checkbox, :radio').prop('checked', false);
}

$('.modal #id_valor_diaria, .modal #id_checkin, .modal #id_pre_checkout, .modal #id_checkout').each(function(index) {
  // Atribui um número ao id do elemento pra torná-lo único.
  $(this).attr('id', $(this).attr('id') + '_' + index);
  $(this).attr('autocomplete', 'off');
  $(this).datepicker({ dateFormat: 'dd/mm/yy' });
  if ($(this).attr('id') == 'id_pre_checkout' + '_' + index) {
    // Add class
    $(this).addClass('preCheckout');
  }
});

$('.salvar').on('click', function () {
  let form = $(this).closest('form')
  let url = form.attr('action');
  id = $(this).data('id');
  let postData = $(form).serialize();
  $.ajax({
    url: url,
    type: 'POST',
    data: postData,
    success: function (response) {
      $('#myModalPessoa_' + id).on('hidden.bs.modal', function () {
        $('#myModalReserva_' + id).modal('show')
      });
      $('#myModalPessoa_' + id).modal('hide')
      clearForms()
      let formReserva = $('#formReserva' + id)
      $('#id_pessoa_pk_' + id).val(response.pessoa)
    }
  })
});

$('.preCheckout').on('change', function () {
  var valor_diaria = $(this).closest('form').find('input[name="valor_diaria_pk"]');
  // var start = $('#id_checkin').val();
  var start = $(this).closest('form').find('input[name="checkin"]').val();
  var end = $(this).val();
  // Convert date to default format
  var dayStart = start.split('/')[0]
  var monthStart = start.split('/')[1]
  var yearStart = start.split('/')[2]
  var startDateFormated = yearStart + '-' + monthStart + '-' + dayStart
  var dayEnd = end.split('/')[0]
  var monthEnd = end.split('/')[1]
  var yearEnd = end.split('/')[2]
  var endDateFormated = yearEnd + '-' + monthEnd + '-' + dayEnd

  // end - start returns difference in milliseconds
  var startDate = new Date(startDateFormated);
  var endDate = new Date(endDateFormated);
  var millisecondsPerDay = 1000 * 60 * 60 * 24;
  var millisBetween = endDate.getTime() - startDate.getTime();
  var days = millisBetween / millisecondsPerDay;
  // get days
  var valor = valor_diaria.val();
  var valor_total = parseInt(days) * parseInt(valor);
  $('input[name="valor_diaria"').val(valor_total);
});

$('.salvarReserva').on('click', function () {
  let formR = $(this).closest('form')
  let urlR = formR.attr('action');
  id = $(this).data('id');
  let postDataR = $(formR).serialize();
  $.ajax({
    url: urlR,
    type: 'POST',
    data: postDataR,
    success: function (response) {
      location.reload()
    }
  })
});

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
      // $('#id_checkout_nome_cliente').val(item.nome_cliente);
      // $('#id_checkout_quarto').val(item.quarto);
      $('#saldo-devedor').html(item.valor_diaria);
      $('#id_checkout_valor_diaria').val(item.valor_diaria);
      // $('#id_checkout_checkin').val(item.checkin);
      // $('#id_checkout_pre_checkout').val(item.pre_checkout);
      // $('#id_checkout_checkout').val(item.checkout);
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