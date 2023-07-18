import React from 'react';
import axios from 'axios';
import { styled } from '@mui/material/styles';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';

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
  
export default class ReportList extends React.Component {
  state = {
    reports: []
  }
  
  componentDidMount() {
    const headers = {
        "Content-Type": "application/json",
      };

    const url = "http://localhost:8008/report";

    axios.get(url, { headers })
    .then(res => {
    const reports = res.data;
    this.setState({ reports });
    })
  }

  render() {
    return (
        <Box sx={{ p: 10 }}>
            <TableContainer component={Paper}>
                <Table sx={{ minWidth: 700 }} aria-label="customized table">
                    <TableHead>
                    <TableRow>
                        <StyledTableCell>Id</StyledTableCell>
                        <StyledTableCell>Name</StyledTableCell>
                        <StyledTableCell>Assessment date</StyledTableCell>
                        <StyledTableCell>Overall verdict</StyledTableCell>
                    </TableRow>
                </TableHead>
                    <TableBody>
                        {this.state.reports.map((report) => (
                        <StyledTableRow key={report.name}>
                            <StyledTableCell component="th" scope="row">
                            {report.id}
                            </StyledTableCell>
                            <StyledTableCell>{report.name}</StyledTableCell>
                            <StyledTableCell>{report.assessment_date}</StyledTableCell>
                            <StyledTableCell>{report.overall_verdict}</StyledTableCell>
                        </StyledTableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </Box>
    )
  }
}