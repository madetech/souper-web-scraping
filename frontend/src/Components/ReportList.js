import React, { useState, useEffect }  from 'react';
import { styled } from '@mui/material/styles';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
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

    const [report, setReport] = useState([]);

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
                    <TableBody>
                        { 
                        report?.map((report) => (
                          <StyledTableRow key={report.name}>
                            <StyledTableCell component="th" scope="row">
                            {report.name}
                            </StyledTableCell>
                            <StyledTableCell>{report.assessment_date}</StyledTableCell>
                            <StyledTableCell>{report.overall_verdict}</StyledTableCell>
                            <StyledTableCell>{report.stage}</StyledTableCell>
                        </StyledTableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </Box>
    )
}