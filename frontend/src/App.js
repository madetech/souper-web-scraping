
import React from 'react';
import Navbar from './Components/Navbar';
import ReportList from './Components/ReportList.js';
import CountChart from './Components/charts/CountChart';
// import AverageChart from './Components/charts/AverageChart';

export default function App() {
  return (
    <div className="App">
      <React.Fragment>
        <Navbar 
        />
        <CountChart/>
        {/* <AverageChart/> */}
        <ReportList />
      </React.Fragment>
    </div>
  )
}

