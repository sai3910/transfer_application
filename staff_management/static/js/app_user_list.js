
$(document).ready(function () {

$.fn.dataTable.ext.errMode = 'throw';
  const dataTable = jQuery('#app_user');



  var dt_table = jQuery('#app_user').dataTable({
  // global variable defined in html
    order: [[0, "desc"]],
    lengthMenu: [[10, 25, 50, 75, 100], [10, 25, 50, 75, 100]],
    rowReorder: true,
    scrollY: true,
    scrollX: true,
    columnDefs: [
      {  className: 'reorder', targets: 0 },
      {  className: 'reorder', targets: 1 },
      {  className: 'reorder', targets: 2 },
      {  className: 'reorder', targets: 3 },
      {  className: 'reorder', targets: 4 },
      {  className: 'reorder ', targets: 5 },
      
      // { orderable: true, className: 'reorder', targets: 7},
      // { orderable: true, targets: '_all' },
      {
        // orderable: true,
        // searchable: true,
        className: "center",
        targets: [0, 1, 2, 3, 4, 5, ]
      },
      {
        name: 'email',
        targets: [0],
        // orderable: true,
      },
      {
        name: 'full_name',
        targets: [1],
        // orderable: true,
        // searchable: true,

      },
      {
        name: 'gender',
        targets: [2],
        // orderable: true,
        // searchable: false,

      },
      {
        name: 'school',
        targets: [3],
        // orderable: true,
        // searchable: false,

      },
      {
        name: 'au_points',
        targets: [4],
        // orderable: true,
        // searchable: false,

      },
      {
        name: 'direct_eligible',
        targets: [5],
        // orderable: true,
        // searchable: false,

      },
     

    ],
 
    processing: true,
    serverSide: true,
    stateSave: true,
    ajax: dataTable.attr('data-url'),
  });



});