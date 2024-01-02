import React, { useEffect, useState } from 'react';
import Modalhelper from '../Helpers/ModalHelper';
import Box from '@mui/material/Box';
import { modalStyle } from '../Helpers/ModalStyle';
// import CountChart from 'charts/average';

export default function ChartModal() {
  return (
    <Modalhelper 
    open>
      <Box sx={modalStyle}>
        <h1>Sample text</h1>
        {/* <CountChart.countChart /> */}
      </Box>
    </Modalhelper>
  )
}


