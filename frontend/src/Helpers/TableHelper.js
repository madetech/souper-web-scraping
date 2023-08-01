import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import * as React from 'react';
import { StyledTableCell, StyledTableRow } from './TableProperties';

export default function TableHelper(props) {
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(5);

  const handlePageChange = (event, newPage) => {
    setPage(newPage);
  };

  const handleRowsPerPageChange = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };

  function handleRowClick(row) {
    return props.onRowClickHandler ? props.onRowClickHandler(row) : null;
  }

  return (
    <Box sx={props.style}>
      <Paper sx={{ minwidth: 700 }}>
        <TableContainer sx={{ maxHeight: 700 }}>
          <Table stickyHeader aria-label="sticky table">
            <TableHead sx={{ bgcolor: 'black' }}>
              <StyledTableRow>
                {props.columns.map((column) => (
                  <StyledTableCell key={column.id}>
                    {column.label}
                  </StyledTableCell>
                ))}
              </StyledTableRow>
            </TableHead>

            <TableBody data-testid="tableTest">
              {props.rows
                .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                .map((row) => {
                  return (
                    <StyledTableRow hover role="checkbox" tabIndex={-1} key={row.id} data-testid="rowTest" onClick={() => handleRowClick(row)}>
                      {props.columns.map((column) => {
                        const value = row[column.id];
                        return (
                          <StyledTableCell key={column.id} align={column.align}>
                            {column.format && typeof value === 'number'
                              ? column.format(value)
                              : value}
                          </StyledTableCell>
                        );
                      })}
                    </StyledTableRow>
                  );
                })}
            </TableBody>
          </Table>
        </TableContainer>
        <TablePagination
          rowsPerPageOptions={[5, 10, 50, { value: -1, label: 'All' }]}
          component="div"
          count={props.rows.length}
          rowsPerPage={rowsPerPage}
          page={page}
          onPageChange={handlePageChange}
          onRowsPerPageChange={handleRowsPerPageChange}
        />
      </Paper>
    </Box>
  );
}
