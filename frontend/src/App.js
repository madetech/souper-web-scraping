import React from "react";
import Navbar from "./Components/Navbar";
import ReportList from "./Components/ReportList.js";
import AverageChart from "./Components/charts/AverageChart";
import CountChart from "./Components/charts/CountChart";

export default function App() {
  return (
    <div className="App">
      <Navbar />
      <CountChart />
      <ReportList />
    </div>
  );
}

{
  /* <div className="App">
<Navbar/>
<div class='container'>
<div class='left-component'> <CountChart/></div>
<div class='right-component'> <AverageChart/></div>
</div>
<ReportList />
</div> */
}

// export default function App() {
//   return (
//     <div className="App">
//       <React.Fragment>
//         <Navbar />
//         <CountChart />
//         <AverageChart />
//         <ReportList />
//       </React.Fragment>
//     </div>
//   );
// }
