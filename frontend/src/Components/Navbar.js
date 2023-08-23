import CheckCircleOutlineIcon from '@mui/icons-material/CheckCircleOutline';
import { Typography } from '@mui/material';
import Alert from '@mui/material/Alert';
import Backdrop from '@mui/material/Backdrop';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import CircularProgress from '@mui/material/CircularProgress';
import Dialog from '@mui/material/Dialog';
import { useRef } from 'react';
import "../styles/main.css";
import logo from './Navbar/logo.png';

export default function Navbar(props) {
  const navRef = useRef();

  return (
    <header>
      <nav ref={navRef}>
        <img src={logo} alt="logo" />
        {<Box className="nav-links">
          <Button variant="text" sx={{ color: 'black', textTransform: "none" }} onClick={props.onOpen}>
            Run Scrape
          </Button>
          
          {props.progress == "201" ?
            <Dialog onClose={props.onClose}
              open={props.open}
            >
              <Alert
                iconMapping={{
                  success: <CheckCircleOutlineIcon fontSize="inherit" />,
                }}
              >
                All records scrapped successfully
              </Alert>
            </Dialog>
            :
            <Backdrop
              sx={{ color: '#fff', zIndex: (theme) => theme.zIndex.drawer + 1 }}
              open={props.open}
              onClick={props.onClose}
            >
              <CircularProgress style={{ 'color': 'darkgreen' }} />
              <Typography sx={{ pl: 2 }}>Scrapping in progress...</Typography>
            </Backdrop>
          }
        </Box>}
      </nav>
    </header>
  );
}

