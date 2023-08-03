import TablePagination from '@mui/material/TablePagination';
import * as React from 'react';

export default function Paginationhelper(props) {
  return (


    <TablePagination
      rowsPerPageOptions={[5, 10, 50, { value: -1, label: 'All' }]}
      component="div"
      count={props.count}
      rowsPerPage={props.rowsPerPage}
      page={props.page}
      onPageChange={props.onPageChange}
      onRowsPerPageChange={props.onRowsPerPageChange}
      SelectProps={{
        inputProps: {
          'data-testid': 'rowsDropDown',
        },
        native: true,
        }}
    />


  );
}
