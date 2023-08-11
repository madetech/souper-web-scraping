import ReportList from './Components/ReportList.js';
import Navbar from './Components/Navbar';
import React from 'react';

export default function App() {
  return (
    <div className="App">
      <React.Fragment>
        <Navbar/>
        <ReportList />
      </React.Fragment>
    </div>
  )
}

