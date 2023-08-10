import { fireEvent, render, screen } from '@testing-library/react';
import React, { useState } from 'react';
import TableHelper from '../../Helpers/TableHelper';
import { reportColumns, reports } from "../Fixtures/Reports";

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

describe('<TableHelper />', () => {
    beforeEach(() => {
        mockStateImlementation()
    });


    afterAll(() => {
        jest.resetAllMocks();
    });

    describe('render modal on row click', () => {
        it('trigger row click', async () => {
            const row = jest.fn(setPage(reports[0]));

            render(
                <TableHelper
                    columns={reportColumns}
                    rows={reports}
                    onRowClickHandler={row}
                />
            )

            const firstReportRow = screen.getAllByTestId('rowTest')[0];
            fireEvent.click(firstReportRow);

            expect(row).toHaveBeenCalledTimes(1);
        })
    })
})