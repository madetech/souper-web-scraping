import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Typography from '@mui/material/Typography';
import { styled } from '@mui/material/styles';
import React from 'react';
import Plot from 'react-plotly.js';

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


const style = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: "50%",
  bgcolor: "background.paper",
  p: 8,
  border: '1px solid #000',
};


export default function ModalHelper(props) {

  let metNumbers = 0;
  let notMetNumbers = 0;
  let tbcNumbers = 0;

  {
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

  return (
    <Modal
      open={props.open}
      onClose={() => props.onClose()}
      aria-labelledby="modal-modal-title"
      aria-describedby="modal-modal-description"
    >

      <Box sx={style}>
        <Typography id="modal-modal-title" variant="h6" component="h1">
          {`Sections List: ${props.reportName}`}
        </Typography>

        <Plot
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
        />


        <TableContainer component={Paper}>
          <Table sx={{ minWidth: 700 }} aria-label="customized table">
            <TableHead>
              <TableRow>
                <StyledTableCell>Section number</StyledTableCell>
                <StyledTableCell>Decision</StyledTableCell>
              </TableRow>
            </TableHead>

            <TableBody data-testid='tableTest'>
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


