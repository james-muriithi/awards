$(function () {
    $('#imageUpload').on('change', function () {
        $(this).closest('form').trigger('submit')
    })
})