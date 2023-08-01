import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableContainer from '@mui/material/TableContainer';
import TableFooter from '@mui/material/TableFooter';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import React, { useEffect, useState } from 'react';
import ModalHelper from '../Helpers/ModalHelper';
import PaginationHelper from '../Helpers/PaginationHelper';
import StyledTableCell from '../Helpers/StyledTableCell';
import StyledTableRow from '../Helpers/StyledTableRow';
import getReportList from '../RemoteUseCases/ReportListFetcher';
import getSectionList from '../RemoteUseCases/SectionListFetcher';

export default function ReportList() {
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(5);

  const [report, setReport] = useState([]);
  const [reportId, setReportId] = useState(0);
  const [reportName, setReportName] = useState("");
  const [section, setSection] = useState([]);

  const [open, setOpen] = useState(false);
  const handleClose = () => setOpen(false);
  const handleOpen = () => setOpen(true);

  const emptyRows =
    page > 0 ? Math.max(0, (1 + page) * rowsPerPage - report.length) : 0;
  // Avoid a layout jump when reaching the last page with empty rows.
  const handlePageChange = (
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
    setReport(await getReportList());
    setSection(await getSectionList(reportId));
  }

  useEffect(() => {
    fetchData();
  }, []);

  const handleRowclick = (
    row
  ) => {
    handleOpen();

    {console.log(open)}
    setReportName(row.name);
    setReportId(row.id);
  };

  return (
    <Box>
      <ModalHelper
        open={open}
        onClose={handleClose}
        rowId={reportId}
        reportName={reportName}
        section={section} />

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
              
                  <StyledTableRow data-testid='rowTest' key={row.id} onClick={() => handleRowclick(row)}>
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
                </StyledTableRow>)}
            </TableBody>
            <TableFooter>
              <TableRow>
                <PaginationHelper
                  page={page}
                  handlePageChange={handlePageChange}
                  rowsPerPage={rowsPerPage}
                  handleRowsPerPageChange={handleRowsPerPageChange}
                  reportLength={report.length}
                />
              </TableRow>
            </TableFooter>
          </Table>
        </TableContainer>
      </Box>
    </Box>
  )
}
