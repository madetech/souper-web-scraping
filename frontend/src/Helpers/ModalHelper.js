import Modal from '@mui/material/Modal';
import * as React from 'react';

export default function Modalhelper(props) {
    return (
        <Modal
        open={props.open}
        onClose={() => props.onClose()}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
        data-testid='modalTest'
      >
        {props.children}
      </Modal>
    );
  }
  