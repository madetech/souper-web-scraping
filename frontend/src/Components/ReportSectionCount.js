import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import React, { useEffect, useState } from 'react';
import { reportTableStyle } from '../Helpers/ModalStyle';
import SectionTableHelper from '../Helpers/SectionTableHelper';
import { reportColumns } from '../Helpers/SectionTableProperties';
import getReportList from '../RemoteUseCases/ReportListFetcher';
import SectionModal from './SectionModal';

export default function ReportSectionCount() {
  const [report, setReport] = useState([]);

  useEffect(() => {
    const fetchReport = async () => {
      setReport(await getReportList());
    };

    fetchReport();
  }, [])

  return (
    <Box>
      {
        <SectionModal
          data-testid='sectionTest2' />}
      <Box sx={reportTableStyle}>
        <Typography id="modal-modal-title2" variant="h6" component="h1" sx={{ fontWeight: 'bold' }}>
          Section Count
        </Typography>
        <SectionTableHelper
          style={{ pt: 4 }}
          rows={report}
          columns={reportColumns}
          rowTestId={"reportRowTest"}
        />
      </Box>
    </Box>
  )
}
