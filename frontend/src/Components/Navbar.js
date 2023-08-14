import {useRef} from 'react';
import "../styles/main.css" ;
import logo from './Navbar/logo.png';


function Navbar() {
  const navRef = useRef();


  return ( 
      <header>
          <nav ref={navRef}>
              <img src={logo} alt="logo" />
              <div className="nav-links">
                <a href="/#"> Run scrape</a>
                <a href="/reports"> Reports</a>
                <a href="/#">Data graph</a>
              </div>
          </nav>
      </header>
  );
}

export default Navbar;