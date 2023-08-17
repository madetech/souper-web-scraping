const reports = [
  {
    id: "1",
    assessment_date: "2022-02-03",
    name: "anna",
    overall_verdict: "pass",
    stage: "Alpha"
  },
  {
    id: "2",
    assessment_date: "2021-11-11",
    name: "losy",
    overall_verdict: "pass",
    stage: "Alpha"
  },
  {
    id: "3",
    assessment_date: "2019-10-09",
    name: "jack",
    overall_verdict: "pass",
    stage: "Alpha"
  },
  {
    id: "4",
    assessment_date: "2023-02-05",
    name: "lucas",
    overall_verdict: "pass",
    stage: "Alpha"
  },
  {
    id: "5",
    assessment_date: "2020-12-12",
    name: "emma",
    overall_verdict: "pass",
    stage: "Alpha"
  },
  {
    id: "6",
    assessment_date: "2022-11-10",
    name: "jenna",
    overall_verdict: "pass",
    stage: "Alpha"
  }
];

const reportColumns = [
  { id: 'name', label: 'Name', minWidth: 170 },
  { id: 'assessment_date', label: 'Assessment date', minWidth: 170 },
  { id: 'overall_verdict', label: 'Overall verdict', minWidth: 170 },
  { id: 'stage', label: 'Stage', minWidth: 170 },
];
export { reportColumns, reports };
