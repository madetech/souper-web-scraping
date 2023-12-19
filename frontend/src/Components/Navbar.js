import CheckCircleOutlineIcon from '@mui/icons-material/CheckCircleOutline';
import GetAppIcon from '@mui/icons-material/GetApp';
import LoadingButton from '@mui/lab/LoadingButton';
import Alert from '@mui/material/Alert';
import Box from '@mui/material/Box';
import Dialog from '@mui/material/Dialog';
import React, { useState } from 'react';
import runScrape from '../RemoteUseCases/RunScraper';
import "../styles/main.css";
import logo from './Navbar/logo.png';

export default function Navbar(props) {
  const [scrapeProgress, setScrapeProgress] = useState("");
  const [openDialog, setOpenDialog] = useState(false);
  const [loading, setLoading] = useState(false);


  const handleClickOpenDialog = async () => {
    setLoading(true);
    setOpenDialog(true);
    setScrapeProgress(await runScrape());
  };

  const handleCloseDialog = (value) => {
    setOpenDialog(false);
  };

  return (
    <header>
      <nav>
        <img src={logo} alt="logo" />
        {<Box className="nav-links">
        
          <LoadingButton
            color='success'
            onClick={() => handleClickOpenDialog()}
            loading={scrapeProgress == "201" ?  false : loading}
            loadingPosition="start"
            startIcon={<GetAppIcon />}
            sx={{ color: 'black', textTransform: "none" }}
            variant="text"
          >
           Run scrape
          </LoadingButton>

          {scrapeProgress == "201" ?
            <Dialog onClose={() => handleCloseDialog()}
              open={openDialog}
            >
              <Alert
                iconMapping={{
                  success: <CheckCircleOutlineIcon fontSize="inherit" />,
                }}
              >
                All records scraped successfully please allow a few minutes for analysis to complete
              </Alert>
            </Dialog>
            : null
          }
        </Box>}
      </nav>
    </header>
  );
}

