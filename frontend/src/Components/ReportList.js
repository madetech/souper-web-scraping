import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import React, { useEffect, useState } from 'react';
import { reportTableStyle } from '../Helpers/ModalStyle';
import TableHelper from '../Helpers/TableHelper';
import { reportColumns } from '../Helpers/TableProperties';
import getReportList from '../RemoteUseCases/ReportListFetcher';
import SectionModal from './SectionModal';

export default function ReportList() {
  const [report, setReport] = useState([]);
  const [reportId, setReportId] = useState(0);
  const [reportName, setReportName] = useState("");

  const [open, setOpen] = useState(false);
  const handleClose = () => setOpen(false);
  const handleOpen = () => setOpen(true);

  useEffect(() => {
    const fetchReport = async () => {
      setReport(await getReportList());
    };

    fetchReport();
  }, [])

  const rowClickHandler = async (
    row
  ) => {
    handleOpen();
    setReportName(row.name);
    setReportId(row.id);
  };

  return (
    <Box>
      {open &&
        <SectionModal
          open={open}
          onClose={handleClose}
          rowId={reportId}
          reportName={reportName}
          reportId={reportId}
          data-testid='sectionTest' />}
      <Box sx={reportTableStyle}>
        <Typography id="modal-modal-title" variant="h6" component="h1" sx={{ fontWeight: 'bold' }}>
          Report List
        </Typography>
        <TableHelper
          style={{ pt: 4 }}
          rows={report}
          columns={reportColumns}
          onRowClickHandler={rowClickHandler}
        />
      </Box>
    </Box>
  )
}
