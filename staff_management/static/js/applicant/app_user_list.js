
$(document).ready(function () {


  const dataTable = jQuery('#app_user');


  // function formatStation(d) {
  //   // `d` is the original data object for the row
  //   return `
  //     <table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">
  //       <tr>
  //         <td>Plant:</td>
  //         <td>${d[8]}</td>
  //       </tr>
        
  //     </table>
  //   `;
  // }

  var dt_table = jQuery('#app_user').dataTable({
  // global variable defined in html
    order: [[0, "desc"]],
    lengthMenu: [[10, 25, 50, 75, 100], [10, 25, 50, 75, 100]],
    rowReorder: true,
    scrollY: true,
    scrollX: true,
    columnDefs: [
      { orderable: true, className: 'reorder', targets: 0 },
      { orderable: true, className: 'reorder', targets: 1 },
      { orderable: true, className: 'reorder', targets: 2 },
      { orderable: true, className: 'reorder', targets: 3 },
      { orderable: true, className: 'reorder', targets: 4 },
      { orderable: true, className: 'reorder details-control', targets: 5 },
      { orderable: true, className: 'reorder', targets: 6 },
      // { orderable: true, className: 'reorder', targets: 7},
      { orderable: false, targets: '_all' },
      {
        orderable: true,
        searchable: true,
        className: "center",
        targets: [0, 1, 2, 3, 4, 5, 6, 7]
      },
      {
        name: 'email',
        targets: [0],
        orderable: true,
      },
      {
        name: 'full_name',
        targets: [1],
        orderable: true,
        searchable: true,

      },
      {
        name: 'gender',
        targets: [2],
        orderable: false,
        searchable: false,

      },
      {
        name: 'school',
        targets: [3],
        orderable: false,
        searchable: false,

      },
      {
        name: 'au_points',
        targets: [4],
        orderable: false,
        searchable: false,

      },
      {
        name: 'direct_eligible',
        targets: [5],
        orderable: false,
        searchable: false,

      },
      // {
      //   name: 'created',
      //   targets: [6],
      //   orderable: true,
      //   searchable: true,
      //   "render": function (data, type, row, meta) {
      //     if (type === 'display') {
      //       data = moment(data).format('LLL');
      //     }
      //     return data;
      //   }
      // },
      // {
      //   name: 'modified',
      //   targets: [7],
      //   orderable: true,
      //   searchable: true,
      //   "render": function (data, type, row, meta) {
      //     if (type === 'display') {
      //       data = moment(data).format('LLL');
      //     }
      //     return data;
      //   }
      // },

    ],
    searching: true,
    processing: true,
    serverSide: true,
    stateSave: true,
    ajax: dataTable.attr('data-url'),
  });



  // Add event listener for opening and closing details
  // $('#app_user tbody').on('click', 'td.details-control', function () {
  //   var tr = $(this).closest('tr');
  //   var row = dt_table.api().row(tr);

  //   if (row.child.isShown()) {
  //     // This row is already open - close it
  //     row.child.hide();
  //     tr.removeClass('shown-details-control');
  //   }
  //   else {
  //     // Open this row
  //     row.child(formatStation(row.data())).show();
  //     tr.addClass('shown-details-control');
  //   }
  // });

});