import HighlightOffSharpIcon from '@mui/icons-material/HighlightOffSharp';
import { IconButton } from '@mui/material';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import React, { useState } from 'react';
import Plot from 'react-plotly.js';
import Modalhelper from '../Helpers/ModalHelper';
import { iconStyle, modalStyle } from '../Helpers/ModalStyle';
import TableHelper from '../Helpers/TableHelper';
import { sectionColumns } from "../Helpers/TableProperties";
import FeedbackModal from './FeebackModal';

export default function SectionModal(props) {
  const [open, setOpen] = useState(false);
  const handleClose = () => setOpen(false);
  const handleOpen = () => setOpen(true);
  const [sectionId, setSectionId] = useState(0);
  const [sectionTitle, setSectionTitle] = useState("");

  const rowSectionClickHandler = async (
    row
  ) => {
    handleOpen();
    setSectionId(row.id);
    setSectionTitle(row.title);
  };

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
    <Modalhelper
      open={props.open}
      onClose={props.onClose}
    >
      <Box sx={modalStyle}>
        <Typography id="modal-modal-title" variant="h6" component="h1" sx={{ fontWeight: 'bold' }}>
          {`Sections List: ${props.reportName}`}
        </Typography>

        <FeedbackModal open={open}
          onClose={handleClose}
          sectionTitle={sectionTitle}
          sectionId={sectionId}
        />

        <TableHelper
          style={{ pt: 2 }}
          rows={props.section}
          columns={sectionColumns}
          onRowClickHandler={rowSectionClickHandler}
        />
        <IconButton onClick={() => props.onClose()} style={iconStyle}>
          <HighlightOffSharpIcon />
        </IconButton>
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
    </Modalhelper>
  )
}


