
import React from 'react';
import Navbar from './Components/Navbar';
import ReportList from './Components/ReportList.js';

export default function App() {
  return (
    <div className="App">
      <React.Fragment>
        <Navbar 
        />
        <ReportList />
      </React.Fragment>
    </div>
  )
}

