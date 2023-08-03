import { render, screen } from '@testing-library/react';
import React, { useState } from 'react';
import sections from "./../Fixtures/Sections";
import SectionModal from './SectionModal';

jest.mock('react', () => ({
  ...jest.requireActual('react'),
  useState: jest.fn()
}));

const open = true;
const setOpen = jest.fn();

function mockStateImlementation() {
  const useStateMock = (useState) => [useState, jest.fn()];
  useState.mockImplementation(useStateMock)
  jest
  .spyOn(React, 'useState')
  .mockImplementationOnce(() => [open, setOpen])
}

xdescribe('<SectionModal />', () => {
  beforeEach(() => {
    mockStateImlementation()
  });

  
  afterAll(() => {
    jest.resetAllMocks();
 });
  const handleClose = jest.fn(setOpen(false));

  describe('render modal', () => {
    it('renders table contents', async () => {

      render(<SectionModal 
      open={open} 
      onClose={handleClose}
      rowId={1}
      reportName={'anna'}
      section={sections} />);
      
      const text =  screen.getAllByTestId("modalTest")
      expect(text).toBeInTheDocument();
    });
  })
})
