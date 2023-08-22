import Typography from '@mui/material/Typography';
import React, { useEffect, useState } from 'react';
import Modalhelper from '../Helpers/ModalHelper';
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
      <Typography id="modal-modal-title" variant="h6" component="h1" sx={{ fontWeight: 'bold' }}>
        {`Feedback List for ${props.sectionTitle}`}
      </Typography>
     
      <TableHelper
        style={{ pt: 2 }}
        rows={feedback}
        columns={feedbackColumns}
        onRowClickHandler={null}
        rowTestId={"feedbackRowTest"}
      />
    </Modalhelper>
  )
}


