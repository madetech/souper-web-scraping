import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableRow from '@mui/material/TableRow';
import { styled } from '@mui/material/styles';

const reportColumns = [
  { id: 'name', label: 'Name', minWidth: 170 },
  { id: 'assessment_date', label: 'Assessment date', minWidth: 170 },
  { id: 'overall_verdict', label: 'Overall verdict', minWidth: 170 },
  { id: 'stage', label: 'Stage', minWidth: 170 },
];

const sectionColumns = [
  { id: 'number', label: 'Section Number', minWidth: 170 },
  { id: 'decision', label: 'Decision', minWidth: 170 },
];

const feedbackColumns = [
  { id: 'feedback', label: 'Feedback', minWidth: 170 },
  { id: 'type', label: 'Type', minWidth: 170 },
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

