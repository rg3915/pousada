$('.edit-pessoa').on('click', function (event) {
  event.preventDefault();
  let id = $(this).data('id')
  let modalEdit = $('#myModalEdit_' + id)
  let nome = $(this).data('nome')
  let cpf = $(this).data('cpf')
  let cidade = $(this).data('cidade')
  let estado = $(this).data('estado')
  let endereco = $(this).data('endereco')
  let email = $(this).data('email')
  let telefone = $(this).data('telefone')
  modalEdit.find('#id_nome').val(nome)
  modalEdit.find('#id_cpf').val(cpf)
  modalEdit.find('#id_cidade').val(cidade)
  modalEdit.find('#id_estado').val(estado)
  modalEdit.find('#id_endereco').val(endereco)
  modalEdit.find('#id_email').val(email)
  modalEdit.find('#id_telefone').val(telefone)
});