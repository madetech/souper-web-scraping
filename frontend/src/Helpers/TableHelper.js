import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableSortLabel from "@mui/material/TableSortLabel";
import { visuallyHidden } from "@mui/utils";
import React, { useState } from 'react';
import PaginationHelper from './PaginationHelper';
import { StyledTableCell, StyledTableRow } from './TableProperties';


function descendingComparator(a, b, orderBy) {
  if (b[orderBy] < a[orderBy]) {
    return -1;
  }
  if (b[orderBy] > a[orderBy]) {
    return 1;
  }
  return 0;
}

function getComparator(
  order,
  orderBy
) {
  return order === "desc"
    ? (a, b) => descendingComparator(a, b, orderBy)
    : (a, b) => -descendingComparator(a, b, orderBy);
}

export default function TableHelper(props) {
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(5);
  const [order, setOrder] = useState("asc");
  const [orderBy, setOrderBy] = useState("");
  const handlePageChange = (event, newPage) => {
    setPage(newPage);
  };

  const handleRowsPerPageChange = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };

  const handleRequestSort = (
    event,
    property
  ) => {
    const isAsc = orderBy === property && order === "asc";
    setOrder(isAsc ? "desc" : "asc");
    setOrderBy(property);
  };

  function handleRowClick(row) {
    return props.onRowClickHandler ? props.onRowClickHandler(row) : null;
  }

  function columnWidths(column){
    switch (column) {
      case "name":
        return "40%";
      case "feedback":
        return "80%";
      default:
        return "20%";
    }
  }
  
  const createSortHandler = (property) => (
    event
  ) => {
    handleRequestSort(event, property);
  };

  return (
    <Box sx={props.style}>
      <Paper sx={{ minwidth: 700 }}>
        <TableContainer sx={{ maxHeight: 700 }}>
          <Table stickyHeader aria-label="sticky table">

            <TableHead sx={{ bgcolor: 'black' }}>
              <StyledTableRow>
                {props.columns.map((headCell) => (  
                  <StyledTableCell
                    key={headCell.id}
                    sortDirection={orderBy === headCell.id ? order : false}
                    width={ columnWidths(headCell.id)}
                  >
                    {console.log(headCell.id)}
                    <TableSortLabel
                      active={true}
                      direction={orderBy === headCell.id ? order : "asc"}
                      onClick={createSortHandler(headCell.id)}
                    >
                      {headCell.label}
                      {orderBy === headCell.id ? (
                        <Box component="span" sx={visuallyHidden}>
                          {order === "desc" ? "sorted descending" : "sorted ascending"}
                        </Box>
                      ) : null}
                    </TableSortLabel>
                  </StyledTableCell>
                ))}
              </StyledTableRow>
            </TableHead>


            <TableBody data-testid="tableTest">
              {props.rows.length > 0 && props.rows
                .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                .sort(getComparator(order, orderBy))
                .map((row) => {
                  return (
                    <StyledTableRow hover role="checkbox" tabIndex={-1} key={row.id} data-testid={props.rowTestId} onClick={() => handleRowClick(row)}>
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

        {props.rows.length > 5 &&
        <PaginationHelper
          count={props.rows.length}
          rowsPerPage={rowsPerPage}
          page={page}
          onPageChange={handlePageChange}
          onRowsPerPageChange={handleRowsPerPageChange}
        />}
      </Paper>
    </Box>
  );
}
