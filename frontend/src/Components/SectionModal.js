
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

import React, { useEffect, useState } from 'react';
import Modalhelper from '../Helpers/ModalHelper';
import TableHelper from '../Helpers/TableHelper';
import { sectionColumns, decisionColumns } from "../Helpers/TableProperties";
import getSectionList from '../RemoteUseCases/SectionListFetcher';
import FeedbackModal from './FeedbackModal';

export default function SectionModal(props) {
  const [open, setOpen] = useState(false);
  const handleClose = () => setOpen(false);
  const handleOpen = () => setOpen(true);
  const [section, setSection] = useState([]);
  const [sectionId, setSectionId] = useState(0);
  const [sectionTitle, setSectionTitle] = useState("");


  useEffect(() => {
    const fetchSection = async () => {
      setSection(await getSectionList(props.reportId));
    };

    fetchSection();
  }, [props.reportId])

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
    {
      section.length > 0 && (section).map(sec => {
        switch (sec.decision) {
          case 'Met':
            return metNumbers = metNumbers + 1;
          case 'Not met':
            return notMetNumbers = notMetNumbers + 1;
          case 'TBC':
            return tbcNumbers = tbcNumbers + 1;
          default:
            return 0;
        }
      })
    }
  }

  sumOfDecisionByTypes();
  const decison = [
    {
      id: '1', decisionType: "Met", total: metNumbers
    },
    {
      id: '2', decisionType: "Not Met", total: notMetNumbers
    },
    {
      id: '3', decisionType: "TBC", total: tbcNumbers
    },
  ]
  return (
    <Modalhelper
      open={props.open}
      onClose={props.onClose}
    >
      <Typography id="modal-modal-title" variant="h6" component="h1" sx={{ fontWeight: 'bold' }}>
        {`Sections List: ${props.reportName}`}
      </Typography>

      {open &&
        <FeedbackModal open={open}
          onClose={handleClose}
          sectionTitle={sectionTitle}
          sectionId={sectionId}
          data-testid='feedbackTest'
        />
      }

      <TableHelper
        style={{ pt: 2 }}
        rows={section}
        columns={sectionColumns}
        onRowClickHandler={rowSectionClickHandler}
        rowTestId={"sectionRowTest"}
      />

      <TableHelper
        style={{ pt: 6, pl: 10, pr: 10}}
        rows={decison}
        columns={decisionColumns}
        rowTestId={"decisionRowTest"}
        onRowClickHandler={rowSectionClickHandler}
      />
    </Modalhelper>
  )
}


