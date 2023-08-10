import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import React, { useEffect, useState } from 'react';
import { reportTableStyle } from '../Helpers/ModalStyle';
import TableHelper from '../Helpers/TableHelper';
import { reportColumns } from '../Helpers/TableProperties';
import getReportList from '../RemoteUseCases/ReportListFetcher';
import getSectionList from '../RemoteUseCases/SectionListFetcher';
import SectionModal from './SectionModal';

export default function ReportList() {
  const [report, setReport] = useState([]);
  const [reportId, setReportId] = useState(0);
  const [reportName, setReportName] = useState("");
  const [section, setSection] = useState([]);

  const [open, setOpen] = useState(false);
  const handleClose = () => setOpen(false);
  const handleOpen = () => setOpen(true);

  useEffect(() => {
    const fetchReport = async () => {
      setReport(await getReportList());
    };

    const fetchSection = async () => {
      setSection(await getSectionList(reportId));
    };

    fetchReport();
    fetchSection();
  }, [reportId])

  const rowClickHandler = async (
    row
  ) => {
    handleOpen();
    setReportName(row.name);
    setReportId(row.id);
  };

  return (
    <Box>
      <SectionModal
        open={open}
        onClose={handleClose}
        rowId={reportId}
        reportName={reportName}
        section={section} />
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
