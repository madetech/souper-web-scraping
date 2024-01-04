import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import React, { useState } from 'react';
import { StyledTableCell, StyledTableRow } from './SectionTableProperties';


export default function SectionTableHelper(props) {
  const [rowsPerPage] = useState(2);

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
                  >
                    {console.log(headCell.id)}
                    {headCell.label}
                  </StyledTableCell>
                ))}
              </StyledTableRow>
            </TableHead>

            <TableBody data-testid="tableTest">
              {props.rows.length > 0 && props.rows
                .slice(0, rowsPerPage)
                .map((row) => {
                  return (
                    <StyledTableRow tabIndex={-1} key={row.id} data-testid={props.rowTestId}>
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
      </Paper>
    </Box>
  );
}
