import pandas as pd


class Restructure:

    def __init__(self, file_path, sheet_name, out_path):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.out_path = out_path

        self._set_df_from_excel()
        self._set_date_and_number_ranges()

    # Generate dataframe from input sheet
    def _set_df_from_excel(self):
        self.df = pd.read_excel(io=self.file_path, sheet_name=self.sheet_name, header=None)

    def _set_date_and_number_ranges(self):
        self.start_date = self.df.iloc[0, 0]
        print('Start date is', self.start_date)
        self.end_date = self.df.iloc[1, 0]
        print('End date is', self.end_date)

        # Get time delta +1 day which is first day
        self.number_of_days = (self.end_date - self.start_date).days + 1
        print('Number of days is', self.number_of_days)

        # Range of days based on date difference
        self.day_range = range(1, self.number_of_days + 1)
        # Range of dates generated from start
        self.date_range = pd.date_range(start=self.start_date, end=self.end_date).date

    def restructure_analytics_data(self) -> None:
        row_count = len(self.df)
        column_count = len(self.df.columns)

        # Save each site dataframe
        frames = []

        # Get date count adn date ranges from input

        # Loop over rows 3 at a time to get each Site separate
        for i in range(0, row_count - 1, 3):
            tmp_df = pd.DataFrame({
                # Set day number range incrementally
                'Day of Month': self.day_range,
                # Set date range incrementally
                'Date': self.date_range,
                # Get site id by index
                'Site ID': self.df.iloc[i + 3, 0],
            })

            # Loop over every attribute bulk at a time to extract its values
            for j in range(0, column_count - 1, self.number_of_days):
                # Get current column header
                curr_header = self.df.iloc[i + 1, j + 1]
                # Get row values for current attribute
                data = self.df.iloc[i + 3, j + 1:j + self.number_of_days + 1].values
                # Set current column with respective values
                tmp_df[curr_header] = data

            # Save dataframe to list of dataframes
            frames.append(tmp_df)

        # Result as concatenation of all Sites into one DataFrame
        self.result = pd.concat(frames)

        self._write_to_out_file()
        return True


    def _write_to_out_file(self):
        # Write result to excel
        self.result.to_excel(self.out_path, sheet_name=f'output_{str(self.number_of_days)}_days_report', index=False)
