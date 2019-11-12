$('.edit-quarto').on('click', function (event) {
  event.preventDefault();
  let id = $(this).data('id')
  let modalEdit = $('#myModalEdit_' + id)
  let numero = $(this).data('numero')
  let titulo = $(this).data('titulo')
  let padrao = $(this).data('padrao')
  let diaria = $(this).data('diaria').replace(',', '.')
  let observacoes = $(this).data('observacoes')
  modalEdit.find('#id_numero').val(numero)
  modalEdit.find('#id_titulo').val(titulo)
  modalEdit.find('#id_padrao').val(padrao)
  modalEdit.find('#id_valor_diaria').val(diaria)
  modalEdit.find('#id_observacoes').val(observacoes)
});