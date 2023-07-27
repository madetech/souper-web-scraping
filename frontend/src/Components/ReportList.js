import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableFooter from '@mui/material/TableFooter';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import { styled } from '@mui/material/styles';
import React, { useEffect, useState } from 'react';
import PaginationHelper from '../Helpers/PaginationHelper';
import getList from "../RemoteUseCases/GetReportList";

const StyledTableCell = styled(TableCell)(({ theme }) => ({
    [`&.${tableCellClasses.head}`]: {
      backgroundColor: theme.palette.common.black,
      color: theme.palette.common.white,
    },
    [`&.${tableCellClasses.body}`]: {
      fontSize: 14,
    },
  }));
  
const StyledTableRow = styled(TableRow)(({ theme }) => ({
'&:nth-of-type(odd)': {
    backgroundColor: theme.palette.action.hover,
},
// hide last border
'&:last-child td, &:last-child th': {
    border: 0,
},
}));


export default function ReportList(props) {
    const [page, setPage] = useState(0);
    const [rowsPerPage, setRowsPerPage] = useState(5);
    const [report, setReport] = useState([]);
    
    const emptyRows =
      page > 0 ? Math.max(0, (1 + page) * rowsPerPage - report.length) : 0;
    // Avoid a layout jump when reaching the last page with empty rows.
    const handlePageChange = (
        event,
        newPage
      ) => {
          setPage(newPage);
      };
    
      const handleRowsPerPageChange = (
        event,
      ) => {
        setRowsPerPage(parseInt(event.target.value, 10));
        setPage(0);
      };
    
    async function fetchData() {
      setReport(await getList());
    }
  
    useEffect(() => {
       fetchData();
    }, []);
 
    return (
      
        <Box sx={{ p: 10 }}>
            <TableContainer component={Paper}>
                <Table sx={{ minWidth: 700 }} aria-label="customized table">
                    
                    <TableHead>
                        <TableRow>
                            <StyledTableCell>Name</StyledTableCell>
                            <StyledTableCell>Assessment date</StyledTableCell>
                            <StyledTableCell>Overall verdict</StyledTableCell>
                            <StyledTableCell>Stage</StyledTableCell>
                        </TableRow>
                    </TableHead>
  
               
                    <TableBody data-testid='tableTest'>     
                     {(rowsPerPage > 0
                            ? report.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                            : report).map((row) => (

                            <StyledTableRow key={row.id}>
                                <StyledTableCell component="th" scope="row">
                                {row.name}  
                                </StyledTableCell>
                                <StyledTableCell>{row.assessment_date}</StyledTableCell>
                                <StyledTableCell>{row.overall_verdict}</StyledTableCell>
                                <StyledTableCell>{row.stage}</StyledTableCell>
                            </StyledTableRow>  
                        ))}
                        </TableBody>
  
                    <TableBody data-testid='tableTest1'>     
                      {emptyRows > 0 && (
                          <StyledTableRow style={{ height: 53 * emptyRows }}>
                              <StyledTableCell colSpan={6} />
                          </StyledTableRow> )}  
                    </TableBody>
                    <TableFooter>
                        <TableRow>
                          <PaginationHelper 
                            page={page} 
                            handlePageChange= {handlePageChange}
                            rowsPerPage={rowsPerPage}
                            handleRowsPerPageChange={handleRowsPerPageChange}
                            reportLength={report.length}
                          />
                        </TableRow>
                    </TableFooter> 
                </Table>
            </TableContainer>
        </Box>
    )
}
