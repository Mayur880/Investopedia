 tinymce.init({
        selector: 'textarea',
//        toolbar: 'imagetools',
//        plugins: 'image imagetools',
//      file_picker_types: 'file image media',
//      file_picker_types: 'file image media',
//       plugins: 'image paste',
//    images_file_types: 'jpg,svg,webp'
     plugins: [
      'advlist autolink link image lists charmap print preview hr anchor pagebreak',
      'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
      'table emoticons template paste help'
    ],
    toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | ' +
      'bullist numlist outdent indent | link image | print preview media fullpage | ' +
      'forecolor backcolor emoticons | help',
    menu: {
      favs: {title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons'}
    },
    menubar: 'favs file edit view insert format tools table help',
    content_css: 'css/content.css'

   });