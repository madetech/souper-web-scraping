import HighlightOffSharpIcon from '@mui/icons-material/HighlightOffSharp';
import { IconButton } from '@mui/material';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import React, { useEffect, useState } from 'react';
import Modalhelper from '../Helpers/ModalHelper';
import { iconStyle, modalStyle } from '../Helpers/ModalStyle';
import TableHelper from '../Helpers/TableHelper';
import { feedbackColumns } from "../Helpers/TableProperties";
import getFeedbackList from '../RemoteUseCases/FeedbackListFetcher';

export default function FeedbackModal(props) {
  const [feedback, setFeedback] = useState([]);

  useEffect(() => {
    const fetchFeedback = async () => {
      setFeedback(await getFeedbackList(props.sectionId));
    };
    fetchFeedback();
  }, [props.sectionId])

  return (
    <Modalhelper
      open={props.open}
      onClose={props.onClose}
    >
      <Box sx={modalStyle}>
        <Typography id="modal-modal-title" variant="h6" component="h1" sx={{ fontWeight: 'bold' }}>
          {`Feedback List for ${props.sectionTitle}`}
        </Typography>
        <TableHelper
          style={{ pt: 2 }}
          rows={feedback}
          columns={feedbackColumns}
          onRowClickHandler={null}
        />
        <IconButton onClick={props.onClose} style={iconStyle}>
          <HighlightOffSharpIcon />
        </IconButton>
      </Box>
    </Modalhelper>
  )
}


