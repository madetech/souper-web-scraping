import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableRow from '@mui/material/TableRow';
import { styled } from '@mui/material/styles';

const reportColumns = [
  { id: 'name', label: 'Name' },
  { id: 'assessment_date', label: 'Assessment date' },
  { id: 'overall_verdict', label: 'Overall verdict' },
  { id: 'stage', label: 'Stage' },
];

const sectionColumns = [
  { id: 'number', label: 'Section Number' },
  { id: 'decision', label: 'Decision' },
];

const feedbackColumns = [
  { id: 'feedback', label: 'Feedback' },
  { id: 'type', label: 'Type' },
];

const StyledTableCell = styled(TableCell)(({ theme }) => ({
  [`&.${tableCellClasses.head}`]: {
    backgroundColor: theme.palette.success.light,
    color: theme.palette.common.white,
  },
  [`&.${tableCellClasses.body}`]: {
    fontSize: 14,
  },
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
  '&:nth-of-type(odd)': {
    backgroundColor: theme.palette.action.hover,
  },
  // hide last border
  '&:last-child td, &:last-child th': {
    border: 0,
  },
}));

export { StyledTableCell, StyledTableRow, feedbackColumns, reportColumns, sectionColumns };

