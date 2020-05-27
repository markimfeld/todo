$(document).ready(function(){
    $('#btnCreateTask').click(() => {
        let serializeData = $('#newTaskForm').serialize();
        $.ajax({
            url: $('#newTaskForm').data('url'),
            data: serializeData,
            type: 'post',
            success: function(response) {
                $('#listTask').append(
                    `
                    <li class="list-group-item d-flex justify-content-between">
                        <span>${response.task.name}</span>
                        <a href="delete/${response.task.id}"><i class="fas fa-minus"></i></a>
                    </li>
                    `
                );
                $('#id_name').val('');
            }
        })
    });
});