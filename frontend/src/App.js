
import React, { useState } from 'react';
import Navbar from './Components/Navbar';
import ReportList from './Components/ReportList.js';
import runScrape from './RemoteUseCases/RunScraper';

export default function App() {
  const [scrapeProgress, setScrapeProgress] = useState("");
  const [openDialog, setOpenDialog] = useState(false);

  const handleClickOpenDialog = async () => {
    setOpenDialog(true);
    setScrapeProgress(await runScrape())
  };

  const handleCloseDialog = (value) => {
    setOpenDialog(false);
  };


  return (
    <div className="App">
      <React.Fragment>
        <Navbar 
        onClose={handleCloseDialog} 
        onOpen={handleClickOpenDialog} 
        open={openDialog} 
        progress={scrapeProgress}
        />
        <ReportList />
      </React.Fragment>
    </div>
  )
}

