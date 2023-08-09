import HighlightOffSharpIcon from '@mui/icons-material/HighlightOffSharp';
import { IconButton } from '@mui/material';
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import * as React from 'react';
import { iconStyle, modalStyle } from '../Helpers/ModalStyle';
export default function Modalhelper(props) {
  return (
    <Modal
      open={props.open}
      onClose={() => props.onClose()}
      aria-labelledby="modal-modal-title"
      aria-describedby="modal-modal-description"
      data-testid='modalTest'
    >
      <Box sx={modalStyle}>
        {props.children}

        <IconButton onClick={() => props.onClose()} style={iconStyle}>
          <HighlightOffSharpIcon />
        </IconButton>
      </Box>
    </Modal>
  );
}
