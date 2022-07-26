import pandas as pd


def get_date_and_number_ranges(df):
    start_date = df.iloc[0, 0]
    print('Start date is', start_date)
    end_date = df.iloc[1, 0]
    print('End date is', end_date)

    # Get time delta +1 day which is first day
    number_of_days = (end_date - start_date).days + 1
    print('Number of days is', number_of_days)

    # Range of days based on date difference
    day_range = range(1, number_of_days + 1)
    # Range of dates generated from start
    date_range = pd.date_range(start=start_date, end=end_date).date

    return number_of_days, day_range, date_range


def restructure_analytics_data(file_path, sheet_name, out_path):
    # Generate dataframe from input sheet
    df = pd.read_excel(io=file_path, sheet_name=sheet_name, header=None)

    row_count = len(df)
    column_count = len(df.columns)

    # Save each site dataframe
    frames = []

    # Get date count adn date ranges from input
    number_of_days, day_range, date_range = get_date_and_number_ranges(df)

    # Loop over rows 3 at a time to get each Site separate
    for i in range(0, row_count - 1, 3):
        tmp_df = pd.DataFrame({
            # Set day number range incrementally
            'Day of Month': day_range,
            # Set date range incrementally
            'Date': date_range,
            # Get site id by index
            'Site ID': df.iloc[i + 3, 0],
        })

        # Loop over every attribute bulk at a time to extract its values
        for j in range(0, column_count - 1, number_of_days):
            # Get current column header
            curr_header = df.iloc[i + 1, j + 1]
            # Get row values for current attribute
            data = df.iloc[i + 3, j + 1:j + number_of_days + 1].values
            # Set current column with respective values
            tmp_df[curr_header] = data

        # Save dataframe to list of dataframes
        frames.append(tmp_df)

    # Result as concatenation of all Sites into one DataFrame
    result = pd.concat(frames)

    # Write result to excel
    result.to_excel(out_path, sheet_name=f'output_{str(number_of_days)}_days_report', index=False)

    return True
