import { render, screen } from '@testing-library/react';
import React from 'react';
import SectionModal from "../../Components/SectionModal";
import sections from "../Fixtures/Sections";

jest.mock("react-plotly.js", () => ({
  __esModule: true,
  default: jest.fn(() => <div />),
}));

describe('<SectionModal />', () => {
  beforeEach(() => {
    const setOpen = jest.fn(x => open)
    const handleClose = jest.fn();
    React.useState = jest.fn()
      .mockImplementationOnce(open => [open, setOpen])

      render(<SectionModal
        open={true}
        onClose={() => handleClose()}
        rowId={1}
        reportName={'anna'}
        section={sections} />);
  });
  
  afterAll(() => {
    jest.resetAllMocks();
  });

  describe('render modal', () => {
    it('renders table contents', async () => {
      expect(screen.getByText('Sections List: anna')).toBeInTheDocument();
    });

    it('renders all section', () => {
      const tableRows = screen.getByTestId('tableTest')
      expect(tableRows.children.length).toBe(sections.length);
    });
  })
})
