import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import Typography from '@mui/material/Typography';
import React from 'react';
import { modalStyle } from '../Helpers/ModalStyle';
import TableHelper from '../Helpers/TableHelper';
import { sectionColumns } from "../Helpers/TableProperties";

export default function SectionModal(props) {
  return (
    <Modal
      open={props.open}
      onClose={() => props.onClose()}
      aria-labelledby="modal-modal-title"
      aria-describedby="modal-modal-description"
      data-testid='modalTest'
    >
      <Box sx={modalStyle}>
        <Typography id="modal-modal-title" variant="h6" component="h1">
          {`Sections List: ${props.reportName}`}
        </Typography>

        <TableHelper
          style={{ pt: 4 }}
          rows={props.section}
          columns={sectionColumns}
          onRowClickHandler={null}
        />
      </Box>
    </Modal>
  )
}


