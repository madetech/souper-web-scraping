import { fireEvent, render, screen } from '@testing-library/react';
import React, { useState } from 'react';
import PaginationHelper from '../Helpers/PaginationHelper';

jest.mock('react', () => ({
  ...jest.requireActual('react'),
  useState: jest.fn()
}));

const page = 0;
const setPage = jest.fn();
const rowsPerPage = 5;
const setRowsPerPage = jest.fn();

function mockStateImlementation() {
  const useStateMock = (useState) => [useState, jest.fn()];
  useState.mockImplementation(useStateMock)
  jest
    .spyOn(React, 'useState')
    .mockImplementationOnce(() => [page, setPage])
    .mockImplementationOnce(() => [rowsPerPage, setRowsPerPage])
}

describe('<PaginationHelper />', () => {
  beforeEach(() => {
    mockStateImlementation()
  });

  afterAll(() => {
    jest.resetAllMocks();
  });

  describe('render pagination', () => {
    it('trigger next page button', () => {
      const onChangePageNo = jest.fn();
      const onRowsPerPageChange = jest.fn();
      render(
        <PaginationHelper
          rowsPerPageOptions={[5, 10, 50, { value: -1, label: 'All' }]}
          component="div"
          count={6}
          rowsPerPage={rowsPerPage}
          page={page}
          onPageChange={onChangePageNo}
          onRowsPerPageChange={onRowsPerPageChange}
        />,
      );

      const nextPageButton = screen.getByRole("button", { name: 'Go to next page' });
      fireEvent.click(nextPageButton);

      expect(onRowsPerPageChange).toHaveBeenCalledTimes(0);
      expect(onChangePageNo).toHaveBeenCalledTimes(1);
    });

    it('trigger previous page button', () => {
      const onChangePageNo = jest.fn();
      const onRowsPerPageChange = jest.fn();
      render(
        <PaginationHelper
          rowsPerPageOptions={[5, 10, 50, { value: -1, label: 'All' }]}
          component="div"
          count={6}
          rowsPerPage={rowsPerPage}
          page={1}
          onPageChange={onChangePageNo}
          onRowsPerPageChange={onRowsPerPageChange}
        />,
      );

      const nextPageButton = screen.getByRole("button", { name: 'Go to previous page' });
      fireEvent.click(nextPageButton);

      expect(onRowsPerPageChange).toHaveBeenCalledTimes(0);
      expect(onChangePageNo).toHaveBeenCalledTimes(1);
    });

    it('change the number of rows per page', async () => {
      
      const onChangePageNo = jest.fn();
      const onRowsPerPageChange = jest.fn();
      render(
        <PaginationHelper
          rowsPerPageOptions={[5, 10, 50, { value: -1, label: 'All' }]}
          component="div"
          count={6}
          rowsPerPage={5}
          page={0}
          onPageChange={onChangePageNo}
          onRowsPerPageChange={onRowsPerPageChange}
        />,
      );

      fireEvent.change(
        screen.getByRole('combobox'),
        screen.getByRole('option', {name: 10}),
      )

      expect(onRowsPerPageChange).toHaveBeenCalledTimes(1);
      expect(onChangePageNo).toHaveBeenCalledTimes(0);
    });
  })
})

