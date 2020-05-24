$(document).ready(() => {

    $('#btnCreateTask').click(function() {
        let serializeData = $('#newTaskForm').serialize();


        // $.ajax({
        //     url: $('#newTaskForm').data('url'),
        //     data: serializeData,
        //     type: 'post',
        //     success: function(response){
        //         console.log(response);
        //     }
        // });
    });

});