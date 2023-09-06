// JavaScript functionality for displaying a preview of the selected image in the post form
$(document).ready(function(){
    $('#id_header_image').change(function(){
        var input = this;
        var url = $(this).val();
        var ext = url.substring(url.lastIndexOf('.') + 1).toLowerCase();
        if (input.files && input.files[0] && (ext == "gif" || ext == "png" || ext == "jpeg" || ext == "jpg")) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#header-image-preview').attr('src', e.target.result);
            }

            reader.readAsDataURL(input.files[0]);
        }
    });
});

//Smooth scrolling feature
$(document).ready(function() {
    $('a[href^="#"]').on('click',function (e) {
      e.preventDefault();
  
      var target = this.hash;
      var $target = $(target);
  
      $('html, body').stop().animate({
          'scrollTop': $target.offset().top
      }, 900, 'swing', function () {
          window.location.hash = target;
      });
    });
  });



