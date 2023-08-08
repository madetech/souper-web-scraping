import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import Typography from '@mui/material/Typography';
import React from 'react';
import Plot from 'react-plotly.js';
import { modalStyle } from '../Helpers/ModalStyle';
import TableHelper from '../Helpers/TableHelper';
import { sectionColumns } from "../Helpers/TableProperties";
export default function SectionModal(props) {

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
    >
       <Box sx={modalStyle}>
        <Typography id="modal-modal-title" variant="h6" component="h1" sx={{ fontWeight: 'bold' }}>
          {`Sections List: ${props.reportName}`}
        </Typography>

        <TableHelper
          style={{ pt: 2 }}
          rows={props.section}
          columns={sectionColumns}
          onRowClickHandler={null}
        />

        <Box sx={{ pt: 2, pl: 8 }}>
          <Plot
          sx={{ pt: 2, pl: 8 }}
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
            layout={{ width: 450, height: 350, title: 'Decisions Plot' }}
          /> 
        </Box>
        
      </Box>
    </Modal>
  )
}


