import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Typography from '@mui/material/Typography';
import React from 'react';
//import Plot from 'react-plotly.js';
import modalStyle from './ModalStyle';
import StyledTableCell from './StyledTableCell';
import StyledTableRow from './StyledTableRow';

export default function ModalHelper(props) {
  let metNumbers = 0;
  let notMetNumbers = 0;
  let tbcNumbers = 0;

  function sumOfDecisionByTypes() {
    (props.section).map(sec => {
      switch (sec.decision) {
        case 'Met':
          return metNumbers = metNumbers + 1;
        case 'Not met':
          return notMetNumbers = notMetNumbers + 1;
        default:
          return tbcNumbers = tbcNumbers + 1;
      }
    })
  }

  sumOfDecisionByTypes();

  return (
    <Modal
      open={props.open}
      onClose={() => props.onClose()}
      aria-labelledby="modal-modal-title"
      aria-describedby="modal-modal-description"
      data-testid='modalTest'
      class='my-modal-class'
    >
      
      <Box sx={modalStyle}>
      
        <Typography id="modal-modal-title" variant="h6" component="h1">
          {`Sections List: ${props.reportName}`}
        </Typography>

        {/* <Plot
          data={[
            {
              x: ["Met", "Not Met", "TBC"],
              y: [metNumbers, notMetNumbers, tbcNumbers],
              type: 'scatter',
              mode: 'lines+markers',
              marker: { color: 'red' },
              name: "decision trace",
            },
            { type: 'bar', x: ["Met", "Not Met", "TBC"], y: [metNumbers, notMetNumbers, tbcNumbers], name: "decision types" },
          ]}
          layout={{ width: 420, height: 340, title: 'Decisions Plot' }}
        /> */}

        <TableContainer component={Paper}>

          <Table sx={{ minWidth: 700 }} aria-label="customized table">
            <TableHead>
              <TableRow>
                <StyledTableCell>Section number</StyledTableCell>
                <StyledTableCell>Decision</StyledTableCell>
              </TableRow>
            </TableHead>

            <TableBody data-testid='modalTableTest'>
              {(props.section).map((sec) => (

                <StyledTableRow key={sec.id}>
                 
                  <StyledTableCell component="th" scope="row">
                    {sec.number}
                  </StyledTableCell>
                  <StyledTableCell>{sec.decision}</StyledTableCell>
                </StyledTableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    </Modal>
  )
}


